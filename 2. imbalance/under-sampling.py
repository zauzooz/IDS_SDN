# https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/

from collections import Counter
from sklearn.datasets import make_classification
from imblearn.under_sampling import RandomUnderSampler

X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)

print(Counter(y))

undersample = RandomUnderSampler(sampling_strategy='majority')

X_over, y_over = undersample.fit_resample(X, y)

print(Counter(y_over))
