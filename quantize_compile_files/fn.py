# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:17:39 2020

@author: Administrator
"""


import numpy as np
import h5py



def calib_input(iter):
    
    


    for i in range(0,2): #24个数据集文件
        ########打开文件#######
        filename ='part'+str(i) + '.h5'
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
    
    X_train=np.array(X_train).reshape(-1,1024,2)
    X_test=np.array(X_test).reshape(-1,1024,2,1)    
    return {"input": X_train}
        # return {X_train,Y_train,Z_train,X_test,Y_test,Z_test}
