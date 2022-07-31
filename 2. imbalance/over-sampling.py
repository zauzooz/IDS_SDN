# https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/

from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler

X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)

print(Counter(y))

oversample = RandomOverSampler(sampling_strategy='minority')

X_over, y_over = oversample.fit_resample(X, y)

print(Counter(y_over))
