import anndata as ad 
import scanpy.api as sc
from sklearn.metrics import silhouette_score, silhouette_samples

def silhouette(adata_name, cluster_annot, value='X_pca', metric='euclidean',
               key_added=None, copy=False):
    """
    Credit to sklearn script : 
    https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py
    return score and silhouette plot. Still some work to do to finish the function.
    size=None but you can put 'large' if you want a bigger default figure size
    """
    
    if copy:
      adata_name = adata_name.copy()
      
    X = adata_name.obsm[value]
    cluster_labels = adata_name.obs[cluster_annot]
    n_clusters = len(set(adata_name.obs[cluster_annot]))

    ## also, return sample_silhouette_values as adata.obs['silhouette_samples']
    silhouette_avg = silhouette_score(X, cluster_labels, metric)
    sample_silhouette_values = silhouette_samples(X, cluster_labels, metric)
    
    if key_added:
        adata_name.obs[key_added] = sample_silhouette_values
        adata_name.uns[key_added] = silhouette_avg
    else:
        adata_name.obs['silhouette_samples'] = sample_silhouette_values
        adata_name.uns['silhouette_samples_avg'] = silhouette_avg

    if copy:
        return(adata_name)
    else:
        return()
