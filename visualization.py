# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:30:38 2022

@author: HP ZBOOK
"""

import matplotlib.pylab as plt
import numpy as np
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:15:44 2022

@author: HP ZBOOK
"""


import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

def dose(t, X):
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0.0, 0.0])
alls = []
fig = plt.figure()
for model in [model1_args, model2_args]:
    args = [
        model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
    ]
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )
    alls.append(sol)
all_specifications= []
all_specifications.append([1,0,0])
all_specifications.append([1,1,1])
 # Perip_Comp = 1, Dose_Comp = True, Protocol = 'Continuous'

def visualization(all_solutions, all_specifications):

    # last row of all_solutions contains the num of peripheral components and dose and protocol types for visualization
    Perip_Comp = []
    Dose_type = []
    Protocol = []

    for spec in all_specifications:
         Perip_Comp.append(spec[0])
         Dose_type.append(spec[1])
         Protocol.append(spec[2])

    if all([i==1 for i in Protocol]) or all([i==0 for i in Protocol]):
        ProtocolHybrid = 0
    else:
        ProtocolHybrid = 1

    # if all([i==1 for i in Dose_type]) or all([i==0 for i in Dose_type]):
    #     DoseTypeHybrid = 0
    # else:
    #     DoseTypeHybrid = 1


    # Map the information from a number to actutal meaning to be shown on fig
    Dose_match = {0: 'intravenous bolus', 1: 'subcutaneous'}
    Protocol_match = {0: 'Delta', 1: 'Continuous'}


    # if there is only one dose/protocol type
    if ProtocolHybrid == 0:
        for k,sol in enumerate(all_solutions[:]):
            plt.plot(sol.t, sol.y[0, :], label= f'model{k+1}'+ '-{}'.format(Dose_match[Dose_type[k]]) +
                     '- q_c')
            if Perip_Comp[k]:
                for i in range(1, Perip_Comp[k]+1):
                    plt.plot(sol.t, sol.y[i, :], label=f'model{k+1}'+ '-{}'.format(Dose_match[Dose_type[k]]) +
                             '- q_p{}'.format(i))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='best')
        plt.title('The model comparision with {} protocol'.format(Protocol_match[Protocol[0]]))
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()


    # if DoseTypeHybrid == 1 and ProtocolHybrid == 0:

    #     fig,axs=plt.subplots(1,2,figsize=(20,10),sharex=False,sharey=False)
    #     fig.suptitle('Model comparision when Dose type of models is hybrid')

    #     for k,sol in enumerate(all_solutions[:]):


    #         if Dose_type[k] == 0:
    #             axs[0].plot(sol.t, sol.y[0, :], label= f'model{k+1}' +
    #                       '- q_c')
    #             if Perip_Comp[k]:
    #                 for i in range(1, Perip_Comp[k]+1):
    #                     axs[0].plot(sol.t, sol.y[i, :], label=f'model{k+1}' +
    #                               '- q_p{}'.format(i))


    #         elif Dose_type[k] == 1:

    #              axs[1].plot(sol.t, sol.y[0, :], label= f'model{k+1}' +
    #                       '- q_c')
    #              if Perip_Comp[k]:
    #                 for i in range(1, Perip_Comp[k]+1):
    #                      axs[1].plot(sol.t, sol.y[i, :], label=f'model{k+1}' +
    #                               '- q_p{}'.format(i))
    #     axs[0].set_title('{} with {} protocol'.format(Dose_match[0], Protocol_match[Protocol[0]]))
    #     axs[1].set_title('{} with {} protocol'.format(Dose_match[1], Protocol_match[Protocol[0]]))
    #     axs[0].set_xlabel('time [h]')
    #     axs[0].set_ylabel('drug mass [ng]')
    #     axs[1].set_xlabel('time [h]')
    #     axs[1].set_ylabel('drug mass [ng]')
    #     axs[0].legend()
    #     axs[1].legend()
    #     plt.show()

    if ProtocolHybrid == 1:

        fig,axs=plt.subplots(1,2,figsize=(10,5),sharex=False,sharey=False)
        fig.suptitle('Model comparision when Protocol type of models is hybrid')

        for k,sol in enumerate(all_solutions[:]):


            if Protocol[k] == 0:
                axs[0].plot(sol.t, sol.y[0, :], label= f'model{k+1}'+ '-{}'.format(Dose_match[Dose_type[k]])+'- q_c')
                if Perip_Comp[k]:
                    for i in range(1, Perip_Comp[k]+1):
                        axs[0].plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'.format(Dose_match[Dose_type[k]]) +
                                  '- q_p{}'.format(i))


            elif Protocol[k] == 1:

                 axs[1].plot(sol.t, sol.y[0, :], label= f'model{k+1}' + '-{}'.format(Dose_match[Dose_type[k]])+
                          '- q_c')
                 if Perip_Comp[k]:
                    for i in range(1, Perip_Comp[k]+1):
                         axs[1].plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'.format(Dose_match[Dose_type[k]])+
                                  '- q_p{}'.format(i))
        axs[0].set_title('{} protocol'.format(Protocol_match[Protocol[0]]))
        axs[1].set_title('{} protocol'.format(Protocol_match[Protocol[1]]))
        axs[0].set_xlabel('time [h]')
        axs[0].set_ylabel('drug mass [ng]')
        axs[1].set_xlabel('time [h]')
        axs[1].set_ylabel('drug mass [ng]')
        axs[0].legend()
        axs[1].legend()
        plt.show()

    # if DoseTypeHybrid == 1 and ProtocolHybrid == 1:

    #     fig,axs=plt.subplots(2,2,figsize=(20,10),sharex=False,sharey=False)
    #     fig.suptitle('Model comparision when Protocol and Dose type of models both hybrid')

    #     for k,sol in enumerate(all_solutions[:]):


    #         if Protocol[k] == 0:
    #             axs[0].plot(sol.t, sol.y[0, :], label= f'model{k+1}' +
    #                       '- q_c')
    #             if Perip_Comp[k]:
    #                 for i in range(1, Perip_Comp[k]+1):
    #                     axs[0].plot(sol.t, sol.y[i, :], label=f'model{k+1}' +
    #                               '- q_p{}'.format(i))


    #         elif Protocol[k] == 1:

    #              axs[1].plot(sol.t, sol.y[0, :], label= f'model{k+1}' +
    #                       '- q_c')
    #              if Perip_Comp[k]:
    #                 for i in range(1, Perip_Comp[k]+1):
    #                      axs[1].plot(sol.t, sol.y[i, :], label=f'model{k+1}' +
    #                               '- q_p{}'.format(i))
    #     axs[0].set_title('{} with {} protocol'.format(Dose_match[0], Protocol_match[Protocol[0]]))
    #     axs[1].set_title('{} with {} protocol'.format(Dose_match[0], Protocol_match[Protocol[1]]))
    #     axs[0].set_xlabel('time [h]')
    #     axs[0].set_ylabel('drug mass [ng]')
    #     axs[1].set_xlabel('time [h]')
    #     axs[1].set_ylabel('drug mass [ng]')
    #     axs[0].legend()
    #     axs[1].legend()
    #     plt.show()

# fig,axs=plt.subplots(3,3,figsize=(15,15),sharex=True,sharey=False)
# fig.suptitle('The model comparision when dose and protocol type of models are diverse')


# #选中第三行第三个画出散点图
# axs[2][2].scatter(np.random.randn(10),np.random.randn(10))
# axs[2][2].set_title('scatter')
# axs[2][2].set_xlabel('x label')
# axs[2][2].set_ylabel('y label')
# axs[2][2].set_xlim(-5,8)

# #用for循环在第一二行的所有子图框中作图
# for i in range(2):
#     for j in range(3):
#             axs[i][j].plot([2,4,8],range(3))

# plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「是苍啊！」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_46110834/article/details/111461809

visualization(alls,all_specifications)


