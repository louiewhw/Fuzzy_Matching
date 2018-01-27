#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:47:35 2017

@author: Louie
"""
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz, process

Lincense = pd.read_excel('rLincense.xlsx')
HubCus = pd.read_excel('rHubSpotCustomers.xlsx')


def matching():
    
    x = np.array(HubCus.Name,dtype = 'str')
    y = np.array(Lincense.CompanyName, dtype = 'str')
    match = []
    prob = []
    
    for i in x:
        z = process.extractOne(i, y)
    
        match.append(z[0])
        prob.append(z[1])
    
    dic = {'HubCus':x, 'Lincense':match, 'Similarity':prob}
    
    result = pd.DataFrame(dic)
    return result

result = matching()
result = result[['HubCus','Lincense','Similarity']]

