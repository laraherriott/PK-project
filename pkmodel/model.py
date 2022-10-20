#
# Model class
#
import numpy as np
class GaussConvFn():
    """
    This class represents the convolution of a delta function with Gaussian function
    By Gaussian function we mean the pdf of Gaussian distribution.
    The purpose of this function is build up a smooth function which is close to a delta function,
    and enable the numerical solution of ODE using Runge-Kutta method.
    Formally, Let us denote \rho(t)=A * \delta(t-t_center), where A is the magnitude
    \omega(t) = \int \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{t^2}{2\sigma^2}},
    then this class just represent \rho * \omega (t), where * is the convolution.
    See the definition in https://en.wikipedia.org/wiki/Convolution for more information. 
    
    """
    def __init__(self,center: float,magnitude: float,sigma=0.02):
        """
        params:
        center: t_center
        magnitude: magnitude in the delta function
        sigma: sigma in the pdf of Gaussian distribution. 
        
        Note that sigma could not be too small, otherwise ODE solving might fail using Runge-Kutta method.
            
        """
        self.center = center
        self.magnitude = magnitude
        self.sigma = sigma

    def eval_at(self,x:float) -> float:
        '''
        return the value of this function at x 
        '''
        return self.magnitude / (2 * np.pi) ** 0.5 / self.sigma * np.exp(-(x-self.center)**2/(2 * self.sigma ** 2))

class DoseFn():
    """
    This class represents the dose function in the ODE.
    The dose function DOSE(t) should be a linear combination of several pseudo delta function(see GaussConvFn),
    plus a constant value.
    It represents consist of instantaneous doses of X ng of the drug at one or more time points,
    or a steady application of X ng per hour over a given time period, or some combination.
    
    Building up an object needs to specify:
    the stead application dose (constinput)
    A list of instantaneous dosing time and quantity (centerpoints & magnitudes)
    """
    def __init__(self,constinput=0,centerpoints=None,magnitudes=None):
        '''
        params:
        constinput: the steady dose, by default set to 0
        centerpoints: time point of instantaneous doses, should be a list
        magnitudes: amount of instantaneous doses, should be a list (length equal to centerpoints)
        '''
        self.constinput = constinput
        self.deltainput = []
        if centerpoints is not None:
            if len(centerpoints) == len(magnitudes):
                for i in range(len(centerpoints)):
                    self.deltainput.append(GaussConvFn(centerpoints[i],magnitudes[i]))
            else:
                raise ValueError('The length of centerpoints and magnitudes list should be the same!')

    def eval_at(self,x):
        '''
        Return the dose function value at x
        '''
        result = self.constinput
        for i in range(len(self.deltainput)):
            result += self.deltainput[i].eval_at(x)

        return result
class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=42):
        self.value = value

