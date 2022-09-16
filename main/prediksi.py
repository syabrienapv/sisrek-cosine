from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

import pandas as pd
import numpy as np
import scipy as sp
import operator
import os

matrix_path = os.getcwd() + '\\main\\datas\\resep_sparse_matrix.npz'
dataset_path = os.getcwd() + '\\main\\datas\\dataset.csv'

def read_sparse():
    sparse_matrix = sparse.load_npz(matrix_path)
    return sparse_matrix

def read_dataset():
    dataset = pd.read_csv(dataset_path)
    return dataset

def norm_matrix():
    dataset = read_dataset()
    matriks = dataset.pivot_table(index=['user_id'], columns=['title'], values='quantity')
    matriks_norm = matriks.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
    matriks_norm.fillna(0, inplace=True)
    matriks_norm = matriks_norm.T
    matriks_norm = matriks_norm.loc[:, (matriks_norm != 0).any(axis=0)]
    return matriks_norm

def item_similarity():
    matriks_norm = norm_matrix()
    item_similarity = cosine_similarity(read_sparse())
    item_sim_dataset = pd.DataFrame(item_similarity, index = matriks_norm.index, columns = matriks_norm.index)
    return item_sim_dataset

def user_similarity():
    matriks_norm = norm_matrix()
    user_similarity = cosine_similarity(read_sparse().T)
    user_sim_dataset = pd.DataFrame(user_similarity, index = matriks_norm.columns, columns = matriks_norm.columns)
    return user_sim_dataset

def top_item(item_title):
    items = []
    item_sim_dataset = item_similarity()
    count = 1
    # print('item yang sama dengan {} include:\n'.format(item_title))
    for item in item_sim_dataset.sort_values(by = item_title, ascending = False).index[1:11]:
        # print('No. {}: {}'.format(count, item))
        items.append(item)
        count +=1
    return items

