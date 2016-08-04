import numpy as np
import scipy.spatial.distance as sp

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
    n = X.shape[0]
    # cluster allocations for each observation
    cluster_allocations = np.random.choice(k, n)
    # centers of each cluster
    cluster_centers = {key: [] for key in range(k)}

    for kidx in range(k):
        # for every cluster, get all indics for the current allocation
        current_xs_allocated_to_cluster = np.argwhere(cluster_allocations == kidx)
        # derive the mean
        cluster_center = np.mean(X[current_xs_allocated_to_cluster,], axis = 0)
        cluster_centers[kidx] = cluster_center

    # determine the nearest cluster
    for xidx in range(n):
        x = X[xidx,:]
        distances = []
        for kidx in range(k):
            cluster_center = cluster_centers[kidx]
            distances.append(sp.cosine(cluster_center, x))
        cluster_allocations[xidx] = np.argmin(distances)

