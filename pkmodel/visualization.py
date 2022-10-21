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

    # extract the information of specifications into lists
    for spec in all_specifications:
        Perip_Comp.append(spec[0])
        Dose_type.append(spec[1])
        Protocol.append(spec[2])

    # Check whether there is a dose compartment
    if all([i == 1 for i in Protocol]) or all([i == 0 for i in Protocol]):
        ProtocolHybrid = 0
    else:
        ProtocolHybrid = 1

    # Map the information to actutal meaning to be shown on figures
    Dose_match = {0: 'intravenous bolus', 1: 'subcutaneous'}
    Protocol_match = {0: 'Delta', 1: 'Continuous'}

    if ProtocolHybrid == 0:

        # enumerate through all the solutions/models
        for k, sol in enumerate(all_solutions[:]):
            if Dose_type[k]:
                plt.plot(sol.t, sol.y[-1, :],
                         label=f'model{k+1}' + '-dose_comp'
                         )  # draw the dose compartment

                plt.plot(sol.t, sol.y[-2, :], label=f'model{k+1}' + '-{}'
                            .format(Dose_match
                                    [Dose_type[k]
                                     ]
                                    ) + '- q_c')  # draw central compartment
                if Perip_Comp[k]:  # if other peripheral compartments
                    for i in range(0, Perip_Comp[k]):
                        plt.plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                    .format(Dose_match[Dose_type[k]]
                                            ) + '- q_p{}'.format(i+1))
            else:
                plt.plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '-{}'
                            .format(Dose_match
                                    [Dose_type[k]
                                     ]) + '- q_c')  # draw the central compartment
                if Perip_Comp[k]:  # if other peripheral compartments
                    for i in range(0, Perip_Comp[k]):
                        plt.plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                    .format(Dose_match[Dose_type[k]]
                                            ) + '- q_p{}'.format(i+1))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='best')
        plt.title('The model comparision with {} protocol'
                  .format(Protocol_match[Protocol[0]]))
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.savefig('model_visual.png')
        plt.show()

    # If the protocol is hybrid, draw two figures
    # One is the general figure as the above
    # The other contains two subgraphs of each protocol for better comparision
    if ProtocolHybrid == 1:

        for k, sol in enumerate(all_solutions[:]):
            if Dose_type[k]:
                plt.plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '- dose_comp'
                         )  # draw the dose compartment
                plt.plot(sol.t, sol.y[-2, :], label=f'model{k+1}' + '-{}'
                            .format(Dose_match
                                    [Dose_type[k]
                                     ]) + '- q_c')  # draw the central compartment
                if Perip_Comp[k]:  # if other peripheral compartments
                    for i in range(0, Perip_Comp[k]):
                        plt.plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                    .format(Dose_match[Dose_type[k]]
                                            ) + '- q_p{}'.format(i+1))
            else:
                plt.plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '-{}'
                            .format(Dose_match
                                    [Dose_type[k]
                                     ]) + '- q_c')  # draw the central compartment
                if Perip_Comp[k]:  # if other peripheral compartments
                    for i in range(0, Perip_Comp[k]):
                        plt.plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                    .format(Dose_match[Dose_type[k]]
                                            ) + '- q_p{}'.format(i+1))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='best')
        plt.title('The model comparision with {} protocol'
                  .format(Protocol_match[Protocol[0]]))
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.savefig('model_general_visual.png')
        plt.show()

        fig, axs = plt.subplots(1, 2, figsize=(10, 5),
                                sharex=False, sharey=False)
        fig.suptitle('Model comparision when Protocol type is hybrid')

        for k, sol in enumerate(all_solutions[:]):
            if Protocol[k] == 0:
                if Dose_type[k]:
                    axs[0].plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '- dose_comp'
                                )  # draw the dose compartment
                    axs[0].plot(sol.t, sol.y[-2, :], label=f'model{k+1}' + '-{}'
                                .format(Dose_match
                                        [Dose_type[k]
                                         ]) + '- q_c')  # draw the central compartment
                    if Perip_Comp[k]:  # if other peripheral compartments
                        for i in range(0, Perip_Comp[k]):
                            axs[0].plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                        .format(Dose_match[Dose_type[k]]
                                                ) + '- q_p{}'.format(i+1))
                else:
                    axs[0].plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '-{}'
                                .format(Dose_match
                                        [Dose_type[k]
                                         ]) + '- q_c')  # draw the central compartment
                    if Perip_Comp[k]:  # if other peripheral compartments
                        for i in range(0, Perip_Comp[k]):
                            axs[0].plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                        .format(Dose_match[Dose_type[k]]
                                                ) + '- q_p{}'.format(i+1))
            elif Protocol[k] == 1:

                if Dose_type[k]:
                    axs[1].plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '- dose_comp'
                                )  # draw the dose compartment
                    axs[1].plot(sol.t, sol.y[-2, :], label=f'model{k+1}' + '-{}'
                                .format(Dose_match
                                        [Dose_type[k]
                                         ]) + '- q_c')  # draw the central compartment
                    if Perip_Comp[k]:  # if other peripheral compartments
                        for i in range(0, Perip_Comp[k]):
                            axs[1].plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                        .format(Dose_match[Dose_type[k]]
                                                ) + '- q_p{}'.format(i+1))
                else:
                    axs[1].plot(sol.t, sol.y[-1, :], label=f'model{k+1}' + '-{}'
                                .format(Dose_match
                                        [Dose_type[k]
                                         ]) + '- q_c')  # draw the central compartment
                    if Perip_Comp[k]:  # if other peripheral compartments
                        for i in range(0, Perip_Comp[k]):
                            axs[1].plot(sol.t, sol.y[i, :], label=f'model{k+1}' + '-{}'
                                        .format(Dose_match[Dose_type[k]]
                                                ) + '- q_p{}'.format(i+1))
        axs[0].set_title('{} protocol'.format(Protocol_match[Protocol[0]]))
        axs[1].set_title('{} protocol'.format(Protocol_match[Protocol[1]]))
        axs[0].set_xlabel('time [h]')
        axs[0].set_ylabel('drug mass [ng]')
        axs[1].set_xlabel('time [h]')
        axs[1].set_ylabel('drug mass [ng]')
        axs[0].legend()
        axs[1].legend()
        plt.savefig('model_specific_visual.png')
        plt.show()
