import pandas as pd
import os
from pandas import Series,DataFrame

#classic
path_dir_classic = "C:/Users/TTT/Desktop/it/wav_classic"
file_list_classic = os.listdir(path_dir_classic)

classic = {'title' : file_list_classic}
data_classic = DataFrame(classic)
data_classic['label'] = 0
classic_train = data_classic[:131]
classic_test = data_classic[131:]

#pop
path_dir_pop = "C:/Users/TTT/Desktop/it/wav_pop"
file_list_pop = os.listdir(path_dir_pop)

pop = {'title' : file_list_pop}
data_pop = DataFrame(classic)
data_pop['label'] = 1
pop_train = data_pop[:131]
pop_test = data_pop[131:]

#rap
path_dir_rap = "C:/Users/TTT/Desktop/it/wav_rap"
file_list_rap = os.listdir(path_dir_rap)

rap = {'title' : file_list_rap}
data_rap = DataFrame(rap)
data_rap['label'] = 2
rap_train = data_rap[:211]
rap_test = data_rap[211:]

#rnb
path_dir_rnb = "C:/Users/TTT/Desktop/it/wav_rnb"
file_list_rnb = os.listdir(path_dir_rnb)

rnb = {'title' : file_list_rnb}
data_rnb = DataFrame(rnb)
data_rnb['label'] = 3
rnb_train = data_rnb[:511]
rnb_test = data_rnb[511:]

train = pd.concat([classic_train,pop_train,rap_train,rnb_train],axis=0)
test = pd.concat([classic_test,pop_test,rap_test,rnb_test],axis=0)
train
test

import pandas as pd
import librosa
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

    

train_mfcc = []
train_dmfcc = []
train_ddmfcc = []
a=0
for i in train.iloc[:,0]:
    filename = 'C:/Users/TTT/Desktop/it/total_wav/' + i
    
    src, sr = librosa.load(filename)
    mfcc = librosa.feature.mfcc(src, sr, n_mfcc=20)
    dmfcc = mfcc[:, 1:] - mfcc[:, :-1]
    ddmfcc = dmfcc[:, 1:] - dmfcc[:, :-1]
    
    #a = np.concatenate((np.mean(mfcc, axis=1), np.std(mfcc, axis=1), np.mean(dmfcc, axis=1), np.std(dmfcc, axis=1), 
    #                    np.mean(ddmfcc, axis=1), np.std(ddmfcc, axis=1)), axis=0)
    train_mfcc.append(mfcc)
    train_dmfcc.append(dmfcc)
    train_ddmfcc.append(ddmfcc)
    a = a+1
    print(a)
    
    
    
test_mfcc = []
test_dmfcc = []
test_ddmfcc = []
a=0
for i in test.iloc[:,0]:
    filename = 'C:/Users/TTT/Desktop/it/total_wav/' + i
    
    src, sr = librosa.load(filename)
    mfcc = librosa.feature.mfcc(src, sr, n_mfcc=20)
    dmfcc = mfcc[:, 1:] - mfcc[:, :-1]
    ddmfcc = dmfcc[:, 1:] - dmfcc[:, :-1]
    
    #a = np.concatenate((np.mean(mfcc, axis=1), np.std(mfcc, axis=1), np.mean(dmfcc, axis=1), np.std(dmfcc, axis=1), 
    #                    np.mean(ddmfcc, axis=1), np.std(ddmfcc, axis=1)), axis=0)
    test_mfcc.append(mfcc)
    test_dmfcc.append(dmfcc)
    test_ddmfcc.append(ddmfcc)
    a = a+1
    print(a)



    
    