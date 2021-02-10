from sklearn .datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


data = load_breast_cancer()
print(data.feature_name)
print(data.target_name)
