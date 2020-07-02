# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:30:14 2020

@author: Carlota
"""
import numpy as np
import pandas as pd
import operator
import statistics
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder

#check https://scikit-learn.org/stable/modules/cross_validation.html for more on cross validation, it explains the basic principle and how the splitting of the data works
"""
def get_partitions(X, y):
    skf = StratifiedKFold(n_splits=10, shuffle = True)
    skf.get_n_splits(X, y)
    
    for train_index, test_index in skf.split(X, y):
        #print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    return X_train
"""
def performance_baselines(X_train, X_test, y_train, y_test):

    cutoffs = list(np.arange(0.01, 1, 0.01)) #different thresholds to test with the training test
    max_cutoff, f1_test = performance_baseline(X_train, X_test, y_train, y_test, cutoffs)
    return max_cutoff, f1_test


def calculate_f1_score(interaction_similarities, interactions, thresh): #predict interactions for a given threshold and calculate f1 score
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    pos_precision = 0
    pos_recall = 0
    
    final_f1_score = 0

    for i in range(len(interactions)):
        prediction = 1 if interaction_similarities[i] >= thresh else 0
        if interactions[i] == 1:
            if prediction == 1:
                TP += 1
            else:
                FN += 1
        else:
            if prediction == 1:
                FP += 1
            else:
                TN += 1
	
    if TP+FP != 0:
        pos_precision = TP / (TP+FP)
    if TP+FN != 0:
        pos_recall = TP / (TP+FN)
        
    if pos_recall + pos_precision != 0:
        final_f1_score = 2 * (pos_precision * pos_recall) / (pos_precision + pos_recall)
    return final_f1_score

def performance_baseline(X_train, X_test, y_train, y_test, cutoffs): 

    F1_TrainingSet = {} #dictionary to store the f1 value for each threshold in a training set
    for cutoff in cutoffs:
        F1_TrainingSet[cutoff] = calculate_f1_score(X_train, y_train, cutoff) #calculate f1 score for the training set at the given threshold
        
    max_cutoff = max(F1_TrainingSet.items(), key=operator.itemgetter(1))[0] #selects the threshold that produces the highest f1 score (max_cutoff) in the training set
    
    f1_test = calculate_f1_score(X_test, y_test, max_cutoff) #uses max_cutoff to calculate f1 score in the test set and returns the f1 score for that threshold
   

    return max_cutoff, f1_test


def get_threshold_10fold_cv (new_ssm, benchmark_dataset):
    df = pd.read_csv(benchmark_dataset, sep = ';')
    df = df.values
    
    y = np.array(df[:,2]) #Interactions
    X = np.array(new_ssm) #Similarity value for each pair
    
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y) #Interpret columns in Y as 2 classes: 0 and 1
    #n = 1
    
    skf = StratifiedKFold(n_splits=10, shuffle = True) #Defines how each array (x and y) will be splitted
    skf.get_n_splits(X, y) #split X and Y
    
    best_cutoffs = [] #list of the thresholds with the best f1 score for each set 
    
    for train_index, test_index in skf.split(X, y): #define test and training sets
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        max_cutoff, f1_test = performance_baselines(X_train, X_test, y_train, y_test)
        best_cutoffs.append(max_cutoff)
    #print('Partition: '+str(n)+'\tThreshold:'+str(max_cutoff)+'\tF1-score:'+str(f1_test))
    #n += 1
    cutoff = statistics.median(best_cutoffs) #Not sure if this is the correct way, but given a list of the best scoring thresholds, I chose the median as the best threshold for this dataset. This will then be used to calculate the f1 score in the whole dataset. 
    return cutoff
