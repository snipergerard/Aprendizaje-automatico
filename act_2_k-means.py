import numpy as np
import matplotlib.pyplot as plt

def kmeans(X, k, max_iters=100):
    #Primero que nada, inicializamos k puntos al azar como centroides iniciales
    np.random.seed(42)
    indices_aleatorios = np.random.choice(len(X), k, replace=False)
    centroides = X[indices_aleatorios]

    for _ in range(max_iters):
        #2. Asginacion: Calculamos la distancia de cada punto a todos los centroides 
        #Usamos norma euclidiana
        distancias = np.linalg.norm(X[:, np.newaxis] - centroides, axis=2)


        #Cada punto se asigna al indice del centroide mas cercano..
        etiquetas = np.argmin(distancias, axis=1)


        #3. Actualizacion: Recalculamos los centroides sacando la media de los puntos del grupo
        nuevos_centroides = np.array([X[etiquetas == i].mean(axis=0) for i in range(k)])


        #4. Convergencia: Si los centroides ya no se mueven, terminamos
        if np.allclose(centroides, nuevos_centroides):
            break

        centroides = nuevos_centroides

    return etiquetas, centroides
# Ejemplo rapido para probarlo
from sklearn.datasets import make_blobs

#Seguido a eso generamos datos sinteticos (3 Grupoos)

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)

#Generamos nuestro algoritmo con k=3
etiquetas, centroides = kmeans(X, k=3)

#Visualizacion osi osi
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', s=50)
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, marker='X', label='Centroides')
plt.legend()
plt.show()
