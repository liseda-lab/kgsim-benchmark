import pandas as pd
import numpy as np
import sklearn.metrics
import matplotlib.pyplot as plt
import precisionRecall as pr
import crossvalidation as cv

colors = ['tab:blue', 'tab:green', 'tab:red', 'tab:orange', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

def calculate_f1_score(interaction_similarities, interactions, thresh):
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
    return pos_precision, pos_recall, final_f1_score
       
def get_f1_score_df(benchmark_dataset, measures, thresh):
    df = pd.read_csv(benchmark_dataset, delimiter =';')
    df = df.values
    interactions = df[:,2]
    
    bma_resnik_p, bma_resnik_r, bma_resnik_f1 = calculate_f1_score(df[:,3], interactions, thresh)
    bma_seco_p, bma_seco_r, bma_seco_f1 = calculate_f1_score(df[:,4], interactions, thresh)    
    gic_resnik_p, gic_resnik_r, gic_resnik_f1 = calculate_f1_score(df[:,5], interactions, thresh)    
    gic_seco_p, gic_seco_r, gic_seco_f1 = calculate_f1_score(df[:,6], interactions, thresh)
    
    
    d = {'metric': ['Precision','Recall', 'F-measure'], 
             'BMA Resnik': [bma_resnik_p, bma_resnik_r, bma_resnik_f1], 
             'BMA Seco': [bma_seco_p, bma_seco_r, bma_seco_f1], 
             'GIC Resnik': [gic_resnik_p, gic_resnik_r, gic_resnik_f1], 
             'GIC Seco': [gic_seco_p, gic_seco_r, gic_seco_f1]}
    
    for ssm in measures:
        ssm_p, ssm_r, ssm_f1 = calculate_f1_score(measures[ssm], interactions, thresh)
        d[ssm] = [ssm_p, ssm_r, ssm_f1]
    
    df_f1 = pd.DataFrame(data = d) 
    return df_f1

def plot_f1(df, colors = colors, size = 50):    
    labels = list(df.columns)[1:]
    points = []
    columns = list(df)[1:] 
    
    for i in columns:
        precision = df[i][0]
        recall = df[i][1]
        points.append([precision, recall])
    
    pr.plotPrecisionRecallDiagram(points,labels, colors, size)


def plot_precision_recall(benchmark_dataset, measures, benchmark_measures = True, col = colors):
    df = pd.read_csv(benchmark_dataset, delimiter =';')
    df = df.values
    y_true = df[:,2]
    y_true_a = np.array(y_true).astype(int)
    
    i = 0
    d = {'metric': ['Best Threshold','Precision', 'Recall', 'F1-score']}
    for ssm in measures:
        y_scores_a = np.array(measures[ssm]).astype(float) 
        
        precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y_true_a, y_scores_a)
        plt.plot(recall, precision, color = col[i], label = ssm)
            
        #higher threshold with 10-fold cross validation            
        higher_threshold = cv.get_threshold_10fold_cv(measures[ssm], benchmark_dataset)
        pos_precision, pos_recall, final_f1_score = calculate_f1_score(measures[ssm], y_true, higher_threshold)
        d[ssm] = [higher_threshold, pos_precision, pos_recall, final_f1_score]
        i+=1
    
    if benchmark_measures:
        bench_measures = {'BMA Resnik':df[:,3], 
             'BMA Seco': df[:,4], 
             'GIC Resnik': df[:,5], 
             'GIC Seco':df[:,6]}
        for measure in bench_measures:
            y_scores_a = np.array(bench_measures[measure]).astype(float)
            precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y_true_a, y_scores_a)
            plt.plot(recall, precision, color = col[i], label = measure)

            
            higher_threshold = cv.get_threshold_10fold_cv(bench_measures[measure], benchmark_dataset)
            pos_precision, pos_recall, final_f1_score = calculate_f1_score(bench_measures[measure], y_true, higher_threshold)
            d[measure] = [higher_threshold, pos_precision, pos_recall, final_f1_score]
            i+=1
    
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    plt.legend(loc = (1.01, 0))
    df_f1 = pd.DataFrame(data = d)
    return df_f1


def interaction_dataset(dataset_type):
    dataset_type = dataset_type.lower()
    return dataset_type == 'ppi'