# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:49:16 2020

@author: Carlota
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
   
def molecular_function_dataset(dataset_type):
    dataset_type = dataset_type.lower()
    return dataset_type == 'mf'

def extract_new_ssm(test_dataset, sep = ';', head = 0, col_n = -1):
    df = pd.read_csv(test_dataset, delimiter = sep, header = head)
    df = df.values
    return df[:,col_n]

def pearson_correlation(benchmark_dataset, measures, dataset_type):
    dataset_type = dataset_type.lower()
    bmd = pd.read_csv(benchmark_dataset, delimiter =';')
    pearsoncorr = bmd.corr(method='pearson')    
    bmd = bmd.values
    seq = bmd[:,-1]
    
    #new_ssm_seq = np.corrcoef(new_ssm.astype(float), seq.astype(float), rowvar = False)[0,-1]
    if  dataset_type == 'mf':
        bma_resnik_seq = pearsoncorr.iloc[0,-1]
        bma_seco_seq = pearsoncorr.iloc[1,-1]
        gic_resnik_seq = pearsoncorr.iloc[2,-1]
        gic_seco_seq = pearsoncorr.iloc[3,-1]
        bma_resnik_pfam = pearsoncorr.iloc[0,-2]
        bma_seco_pfam = pearsoncorr.iloc[1,-2]
        gic_resnik_pfam = pearsoncorr.iloc[2,-2]
        gic_seco_pfam = pearsoncorr.iloc[3,-2]
        pfam = bmd[:, -2]
        #new_ssm_pfam = np.corrcoef(new_ssm.astype(float), pfam.astype(float), rowvar = False)[0,-1] 
        d = {'similarity proxy': ['sequence','molecular function'], 
             'BMA Resnik': [bma_resnik_seq, bma_resnik_pfam], 
             'BMA Seco': [bma_seco_seq, bma_seco_pfam], 
             'GIC Resnik': [gic_resnik_seq, gic_resnik_pfam], 
             'GIC Seco': [gic_seco_seq, gic_seco_pfam]}
        for ssm in measures:
            new_ssm_pfam = np.corrcoef(measures[ssm].astype(float), pfam.astype(float), rowvar = False)[0,-1]
            new_ssm_seq = np.corrcoef(measures[ssm].astype(float), seq.astype(float), rowvar = False)[0,-1]
            d[ssm] = [new_ssm_seq, new_ssm_pfam]
        table = pd.DataFrame(data = d)
    elif dataset_type == 'ppi':
        bma_resnik_seq = pearsoncorr.iloc[1,-1]
        bma_seco_seq = pearsoncorr.iloc[2,-1]
        gic_resnik_seq = pearsoncorr.iloc[3,-1]
        gic_seco_seq = pearsoncorr.iloc[4,-1]
        bma_resnik_ppi = pearsoncorr.iloc[1,0]
        bma_seco_ppi = pearsoncorr.iloc[2,0]
        gic_resnik_ppi = pearsoncorr.iloc[3,0]
        gic_seco_ppi = pearsoncorr.iloc[4,0]
        interactions = bmd[:, 2]
        #new_ssm_ppi = np.corrcoef(new_ssm.astype(float), interactions.astype(float), rowvar = False)[0,-1]         
        d = {'similarity proxy': ['sequence','protein protein interaction'], 
             'BMA Resnik': [bma_resnik_seq, bma_resnik_ppi], 
             'BMA Seco': [bma_seco_seq, bma_seco_ppi], 
             'GIC Resnik': [gic_resnik_seq, gic_resnik_ppi], 
             'GIC Seco': [gic_seco_seq, gic_seco_ppi]}
        for ssm in measures:
            new_ssm_seq = np.corrcoef(measures[ssm].astype(float), seq.astype(float), rowvar = False)[0,-1]
            new_ssm_ppi = np.corrcoef(measures[ssm].astype(float), interactions.astype(float), rowvar = False)[0,-1]
            d[ssm] = [new_ssm_seq, new_ssm_ppi]
        table = pd.DataFrame(data = d)
    else:
        raise ValueError('Not a valid similarity proxy')
    return table       

def pearson_correlation_gene(benchmark_dataset, measures):
    bmd = pd.read_csv(benchmark_dataset, sep = ';')
    pearsoncorr = bmd.corr(method='pearson')
    bmd = bmd.values
    ps = bmd[:,-1]
        
    bma_resnik_ps = pearsoncorr.iloc[0,-1]
    bma_seco_ps = pearsoncorr.iloc[1,-1]
    gic_resnik_ps = pearsoncorr.iloc[2,-1]
    gic_seco_ps = pearsoncorr.iloc[3,-1]
    d = {'similarity proxy': ['phenotypic series'], 
             'BMA Resnik': [bma_resnik_ps], 
             'BMA Seco': [bma_seco_ps], 
             'GIC Resnik': [gic_resnik_ps], 
             'GIC Seco': [gic_seco_ps]}
    for ssm in measures:
        new_ssm_ps = np.corrcoef(measures[ssm].astype(float), ps.astype(float), rowvar = False)[0,-1]
        d[ssm] = new_ssm_ps
    table = pd.DataFrame(data = d)
    return table

def correlation_calculation(benchmark_dataset, measures, dataset_type):
    dataset_type = dataset_type.lower()
    if dataset_type == 'ppi':
        results = pearson_correlation(benchmark_dataset, measures, dataset_type)
    elif dataset_type == 'mf':
        results = pearson_correlation(benchmark_dataset, measures, dataset_type)
    elif dataset_type == 'gene':
        results = pearson_correlation_gene(benchmark_dataset, measures)
    else:
        raise ValueError('Not a type of dataset')
    return results

def plotting_sequence(benchmark_dataset, new_ssm, ssm_name, size = 1, col = 'black'):
    
    bmd = pd.read_csv(benchmark_dataset, delimiter =';')  
    bmd = bmd.values
    
    seq = bmd[:,-1] 
    
    plot = plt.scatter(seq,new_ssm, s = size, c = col)
    plt.ylabel(ssm_name)
    plt.xlabel('Sequence Similarity')
    return plot

def plotting_gene(benchmark_dataset, new_ssm, ssm_name, size = 1, col = 'black'):
    bmd = pd.read_csv(benchmark_dataset, sep = ';')
    bmd = bmd.values
    ps = bmd[:,-1]    
    plot = plt.scatter(ps,new_ssm, s = size, c = col)
    plt.ylabel(ssm_name)
    plt.xlabel('PS Similarity')
    return plot

def plotting_molecular_function(benchmark_dataset, new_ssm, ssm_name, size = 1, col = 'black'):
    
    bmd = pd.read_csv(benchmark_dataset, delimiter =';')  
    bmd = bmd.values
       
    pfam = bmd[:, -2]
    plot = plt.scatter(pfam,new_ssm, s = size, color = col)
    plt.ylabel(ssm_name)
    plt.xlabel('Molecular Function Similarity')
    return plot         

def correlation_plot(benchmark_dataset, new_ssm, dataset_type, ssm_name, size = 1, col = 'black'):
    dataset_type = dataset_type.lower()
    if dataset_type == 'ppi':
        return plotting_sequence(benchmark_dataset, new_ssm, ssm_name, size = size, col = col)
    elif dataset_type == 'gene':
        return plotting_gene(benchmark_dataset, new_ssm, ssm_name, size = size, col = col)
    else:
        raise ValueError('Not a type of dataset')
        
def plot_molecular_function(benchmark_dataset, new_ssm, size= 1, col = 'black'):
    f, ax = plt.subplots(1, 2, figsize=(15,5))  
    
    bmd = pd.read_csv(benchmark_dataset, delimiter =';')  
    bmd = bmd.values
    
    pfam = bmd[:,-2]
    seq = bmd[:,-1] 
    
    ax[0].scatter(seq,new_ssm, s = size, c = col)
    ax[1].scatter(pfam, new_ssm, s = size, c = col)
    return ax