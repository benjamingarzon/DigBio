import pandas as pd
import calendar
import datetime

def index_logic(index):
    if index not in [5, 6]:
        return True
    return False

def read_sleep_file(filename):
    ff = pd.read_csv(filename, skiprows=lambda x: index_logic(x), delimiter=',')
    return ff

def UTC2epoch(x):
    timestamp = pd.Timestamp(x)
    epoch = calendar.timegm(timestamp.utctimetuple())
    #e = datetime.datetime(1970, 1, 1, 0, 0)
    #t = x #datetime.datetime(year, month, day, hour, minute)
    #return (t-e).total_seconds()
    return epoch
  
def read_hr_file(filename):
    ff = pd.read_csv(filename, skiprows=5, delimiter=',')
    return ff
    
def compute_metrics(cm):    
    tn, fp, fn, tp = cm.ravel()
    pos = tp+fn
    neg = tn+fp
    precision = tp/(tp+fp)
    recall = tp/pos
    sensitivity = recall
    specificity = tn/neg
    balanced_acc = 0.5*(tp/pos + tn/neg)
    f1 = 2*(precision*recall)/(precision + recall)
    print("Confusion matrix:")
    print(cm)
    print(f"Precision = {precision:.3f}, Recall = {recall:.3f}, F1 = {f1:.3f}")
    print(f"Sensitivity = {sensitivity:.3f}, Specificity =  {specificity:.3f}")
    print(f"Balanced accuracy =  {balanced_acc:.3f}")