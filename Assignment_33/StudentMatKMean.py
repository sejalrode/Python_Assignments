import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler

def main():
    df = pd.read_csv("student-mat.csv",sep=';')

    for col in df.select_dtypes(include = 'object'):
        df[col] = LabelEncoder().fit_transform(df[col])

    # Select only relevant features for clustering
    features = ["G1", "G2", "G3", "studytime", "failures", "absences"]
    X = df[features].values  

    # Standardize features
    X = StandardScaler().fit_transform(X)

    WCSS = []

    for k in range(1,11):
        model = KMeans(n_clusters = k, init = 'k-means++', n_init = 10, random_state = 42) 
        model.fit(X)
        print(model.inertia_)   #WCSS
        WCSS.append(model.inertia_)

    plt.plot(range(1,11), WCSS, marker = 'o')
    plt.title("Elbow method for KMEANS")
    plt.xlabel("Value of K")
    plt.ylabel("Within Cluster Sum of Square")
    plt.grid(True)
    plt.show()

    model = KMeans(n_clusters = 3, init = 'k-means++', n_init = 10, random_state = 42) 
    y_kmeans = model.fit_predict(X)
    
    # Add cluster labels to dataframe
    df["Cluster"] = y_kmeans

    # Name clusters based on average G3
    cluster_order = df.groupby("Cluster")["G3"].mean().sort_values(ascending=False).index
    mapping = {
        cluster_order[0]: "Top Performers",
        cluster_order[1]: "Average Students",
        cluster_order[2]: "Struggling Students"
    }
    df["Cluster"] = df["Cluster"].map(mapping)

    # Show sample output
    print("\nSample clustered data:")
    print(df[["G1", "G2", "G3", "studytime", "failures", "absences", "Cluster"]].head(10))

    # Print centroids (in original feature scale, not standardized)
    print("\nCluster Centroids (standardized values):")
    centroids = pd.DataFrame(model.cluster_centers_, columns=features)
    print(centroids)

    # Visualization (only first 2 features for simplicity: G1 vs G2)
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=50, c="red", label="Cluster 1")
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=50, c="blue", label="Cluster 2")
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=50, c="green", label="Cluster 3")

    # Plot centroids
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
                s=200, c="yellow", edgecolors="black", marker="X", label="Centroids")

    plt.title("KMeans Clustering of Students")
    plt.xlabel("G1 (standardized)")
    plt.ylabel("G2 (standardized)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

#fit(X) → runs the KMeans algorithm:
#Finds the best positions for the cluster centers (centroids).

#predict(X) → assigns a cluster label (like 0, 1, 2) to each data point based on which centroid it's closest to.

#X[y_kmeans == 0, 0]:	
#Get the X-axis (feature 1) values of all data points assigned to cluster 0

#X[y_kmeans == 0, 1]:	
#Get the Y-axis (feature 2) values of all data points assigned to cluster 0