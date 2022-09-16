# from sklearn.metrics.pairwise import cosine_similarity
# from scipy import sparse
# from  sklearn.neighbors import NearestNeighbors

# import pandas as pd
# import numpy as np
# import scipy as sp
# import operator
# import os

# matrix_path = os.getcwd() + '\\main\\datas\\sparse_matrix_knn.npz'
# dataset_path_rating = os.getcwd() + '\\main\\datas\\rating_knn.csv'
# dataset_path_item = os.getcwd() + '\\main\\datas\\resep_knn.csv'

# def read_sparse():
#     sparse_matrix = sparse.load_npz(matrix_path)
#     return sparse_matrix

# def read_dataset():
#     rating = pd.read_csv(dataset_path_rating, sep=';')
#     item = pd.read_csv(dataset_path_item, sep=';')
#     dataset = pd.merge(item, rating, how='left', on='itemId')
#     return dataset

# def pivot_table():
#     dataset = read_dataset()
#     table = dataset.pivot_table(index='title', columns='userId', values='rating')
#     return table

# def knn_models(itemId):
#     rekomendasi = []
#     model_knn = NearestNeighbors(metric= 'cosine', algorithm= 'brute')
#     matrix = read_sparse()
#     table = pivot_table()
#     model_knn.fit(matrix)
#     distances, indices = model_knn.kneighbors(table.iloc[itemId, :].values.reshape(1, -1), n_neighbors = 6)
#     for i in range(0, len(distances.flatten())):
#         rekomendasi.append(table.index[indices.flatten()[i]])
#     return rekomendasi

# def norm_matrix():
#     dataset = read_dataset()
#     matriks = dataset.pivot_table(index=['userId'], columns=['title'], values='rating')
#     matriks_norm = matriks.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
#     matriks_norm.fillna(0, inplace=True)
#     matriks_norm = matriks_norm.T
#     matriks_norm = matriks_norm.loc[:, (matriks_norm != 0).any(axis=0)]
#     return matriks_norm

# def item_similarity():
#     matriks_norm = norm_matrix()
#     item_similarity = cosine_similarity(read_sparse())
#     item_sim_dataset = pd.DataFrame(item_similarity, index = matriks_norm.index, columns = matriks_norm.index)
#     return item_sim_dataset

# def user_similarity():
#     matriks_norm = norm_matrix()
#     user_similarity = cosine_similarity(read_sparse().T)
#     user_sim_dataset = pd.DataFrame(user_similarity, index = matriks_norm.columns, columns = matriks_norm.columns)
#     return user_sim_dataset

# def top_item(item_title):
#     items = []
#     item_sim_dataset = item_similarity()
#     count = 1
#     # print('item yang sama dengan {} include:\n'.format(item_title))
#     for item in item_sim_dataset.sort_values(by = item_title, ascending = False).index[1:11]:
#         # print('No. {}: {}'.format(count, item))
#         items.append(item)
#         count +=1
#     return items

