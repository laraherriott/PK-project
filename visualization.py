# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:30:38 2022

@author: HP ZBOOK
"""

import matplotlib.pylab as plt


def visualization(all_solutions, all_specifications):
    """
    visualize the drug mass vs time of all model solutions

        Parameters
        ----------
        all_solutions : List
            List of the solution of models containing
            the time and the drug mass vaules
        all_specifications : List
            The list of lists (with three integers per list)
            that specify how many peripheral componets, which
            dose and protocol type for each model.

        Returns
        -------
        None
    """

    Perip_Comp = []
    Dose_type = []
    Protocol = []

    #extract the information of specifications into lists
    for spec in all_specifications:
        Perip_Comp.append(spec[0])
        Dose_type.append(spec[1])
        Protocol.append(spec[2])

    #Check whether the protocols are different from model to model
    if all([i == 1 for i in Protocol]) or all([i == 0 for i in Protocol]):
        ProtocolHybrid = 0
    else:
        ProtocolHybrid = 1

    # Map the information to actutal meaning to be shown on figures
    Dose_match = {0: 'intravenous bolus', 1: 'subcutaneous'}
    Protocol_match = {0: 'Delta', 1: 'Continuous'}

    if ProtocolHybrid == 0:

        #enumerate through all the solutions/models
        for k, sol in enumerate(all_solutions[:]):
            plt.plot(sol.t, sol.y[0, :], label=f'model{k+1}' + '-{}'
                        .format(Dose_match
                                [Dose_type[k]
                                 ]) + '- q_c')  # draw the central compartment
            if Perip_Comp[k]:  # if other peripheral compartments
                for i in range(1, Perip_Comp[k] + 1):
                    plt.plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                .format(Dose_match[Dose_type[k]]
                                        ) + '- q_p{}'.format(i))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='best')
        plt.title('The model comparision with {} protocol'
                  .format(Protocol_match[Protocol[0]]))
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()

    #If the protocol is hybrid, draw a figure
    # contains two subgraphs of each protocol for better comparision
    if ProtocolHybrid == 1:

        fig, axs = plt.subplots(1, 2, figsize=(10, 5),
                                sharex=False, sharey=False)
        fig.suptitle('Model comparision when Protocol type is hybrid')

        for k, sol in enumerate(all_solutions[:]):
            if Protocol[k] == 0:
                axs[0].plot(sol.t, sol.y[0, :], label=f'model{k+1}' + '-{}'
                               .format(Dose_match[Dose_type[k]]) + '- q_c')
                if Perip_Comp[k]:
                    for i in range(1, Perip_Comp[k] + 1):
                        axs[0].plot(sol.t, sol.y[i, :],
                                    label=f'model{k+1}' + '-{}'
                                    .format(Dose_match[Dose_type[k]]
                                            ) + '- q_p{}'.format(i))

            elif Protocol[k] == 1:

                axs[1].plot(sol.t, sol.y[0, :], label=f'model{k+1}' + '-{}'
                               .format(Dose_match[Dose_type[k]]) + '- q_c')
                if Perip_Comp[k]:
                    for i in range(1, Perip_Comp[k] + 1):
                        axs[1].plot(sol.t, sol.y[i, :],
                                    label=f'model{k+1}' + '-{}'
                                       .format(Dose_match[Dose_type[k]]
                                               ) + '- q_p{}'.format(i))
        axs[0].set_title('{} protocol'.format(Protocol_match[Protocol[0]]))
        axs[1].set_title('{} protocol'.format(Protocol_match[Protocol[1]]))
        axs[0].set_xlabel('time [h]')
        axs[0].set_ylabel('drug mass [ng]')
        axs[1].set_xlabel('time [h]')
        axs[1].set_ylabel('drug mass [ng]')
        axs[0].legend()
        axs[1].legend()
        plt.show()



