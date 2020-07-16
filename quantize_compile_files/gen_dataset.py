# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:17:55 2020

@author: Administrator
"""


import h5py
import numpy as np
def create_label():
    classes = ['32PSK',
  '16APSK',
  '32QAM',
  'FM',
  'GMSK',
  '32APSK',
  'OQPSK',
  '8ASK',
  'BPSK',
  '8PSK',
  'AM-SSB-SC',
  '4ASK',
  '16PSK',
  '64APSK',
  '128QAM',
  '128APSK',
  'AM-DSB-SC',
  'AM-SSB-WC',
  '64QAM',
  'QPSK',
  '256QAM',
  'AM-DSB-WC',
  'OOK', 
  '16QAM']
    return classes

def extract_data_set(f,dir_path):
    modu_snr_size = 1200
    for modu in range(24):
        
        
        X_list = [] 
        Y_list = []
        Z_list = []
        print('part ',modu)
        start_modu = modu*106496
        for snr in range(26):
            start_snr = start_modu + snr*4096
            idx_list = np.random.choice(range(0,4096),size=modu_snr_size,replace=False)
            X = f['X'][start_snr:start_snr+4096][idx_list]
          #X = X[:,0:768,:]
            X_list.append(X)
            Y_list.append(f['Y'][start_snr:start_snr+4096][idx_list])
            Z_list.append(f['Z'][start_snr:start_snr+4096][idx_list])

        filename = dir_path + '/part' + str(modu) + '.h5'
        fw = h5py.File(filename,'w')
        fw['X'] = np.vstack(X_list)
        fw['Y'] = np.vstack(Y_list)
        fw['Z'] = np.vstack(Z_list)
        print('X shape:',fw['X'].shape)
        print('Y shape:',fw['Y'].shape)
        print('Z shape:',fw['Z'].shape)
        fw.close()
    f.close()
    
def get_dataset(dir_path):
    for i in range(0,24): #24个数据集文件
        ########打开文件#######
        filename = dir_path + '/part'+str(i) + '.h5'
        print(filename)
        f = h5py.File(filename,'r')
        ########读取数据#######
        X_data = f['X'][:]
        Y_data = f['Y'][:]
        Z_data = f['Z'][:]
        f.close()
        #########分割训练集和测试集#########
        #每读取到一个数据文件就直接分割为训练集和测试集，防止爆内存
        n_examples = X_data.shape[0]
        n_train = int(n_examples * 0.7)   #70%训练样本
        train_idx = np.random.choice(range(0,n_examples), size=n_train, replace=False)#随机选取训练样本下标
        test_idx = list(set(range(0,n_examples))-set(train_idx))        #测试样本下标
        if i == 0:
            X_train = X_data[train_idx]
            Y_train = Y_data[train_idx]
            Z_train = Z_data[train_idx]
            X_test = X_data[test_idx]
            Y_test = Y_data[test_idx]
            Z_test = Z_data[test_idx]
        else:
            X_train = np.vstack((X_train, X_data[train_idx]))
            Y_train = np.vstack((Y_train, Y_data[train_idx]))
            Z_train = np.vstack((Z_train, Z_data[train_idx]))
            X_test = np.vstack((X_test, X_data[test_idx]))
            Y_test = np.vstack((Y_test, Y_data[test_idx]))
            Z_test = np.vstack((Z_test, Z_data[test_idx]))
    print('Xtrain',X_train.shape)
    print('Ytrain',Y_train.shape)
    print('Ztrain',Z_train.shape)
    print('Xtest',X_test.shape)
    print('Ytest',Y_test.shape)
    print('Ztest',Z_test.shape)
    
    return X_train,Y_train,Z_train,X_test,Y_test,Z_test
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    