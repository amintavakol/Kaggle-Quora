#!/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix, vstack, hstack

def read_files(path):
	pass


if __name__ == "__main__":
	train_data = pd.read_csv('data/train.csv')
	train_data.head()
	p = round(train_data['is_duplicate'].mean(), 2)
	print p
	
	test_data = pd.read_csv('data/test.csv')
	sub = pd.DataFrame({'test_id': test_data['test_id'], 'is_duplicate': p})
	sub = sub[['test_id', 'is_duplicate']]
	sub.to_csv('mean_submission.csv', index=False)
	sub.head()