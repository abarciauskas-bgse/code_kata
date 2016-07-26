import numpy as np
from collections import Counter
def kmeans(k, X, niters = 100):
    """
    Executes kmeans clustering algorithm
    ----
    Parameters:
    k - number of clusters
    X - numpy 2-d array of dimensions n - number of obserations, and m - number of features
    niters - number of iterations
    ----
    Returns:
    kclusters - an array of length k, each having length the number of observations of the kth cluster
    """
    n = X.shape()[0]
    m = X.shape()[1]
    kclusters = [[]]*k
    # cluster allocations for each observation
    cluster_allocations = np.random.choice(k, n)
    cluster_size_dict = Counter(cluster_allocations)
    # centers of each cluster
    cluster_centers = np.zeros((k, m))
    for idx in range(n):
        x = X[idx,:]
        x_alloc = cluster_allocations[idx]
        kclusters[x_alloc].append(x)

