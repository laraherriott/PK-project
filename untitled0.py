# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:15:43 2022

@author: HP ZBOOK
"""

class protocol:
    
    def __init__(self, args, protocol = 'intravenous', compartment = 0):
        self.protocol = protocol
        self.args = args
        self.compartment = compartment
        
    def check_protocol(self):
        if self.protocol not in ['intravenous','subcutaneous']:
            raise ValueError("protocol must be 'intravenous' or 'subcutaneous'")
        else:
            print('protocol found:', self.protocol)
        print('compartment num:', self.compartment)
            
            
    def get_arguments(self):
        self.check_protocol()
        if self.protocol == 'intravenous':
            self.args['protocol'] = 'intravenous'
            return self.args
        if self.protocol == 'subcutaneous':
            self.args['protocol'] = 'subcutaneous'
            return self.args
        
        