def generar_caso_de_uso_zonas():
    import numpy as np
    from sklearn.datasets import make_blobs
    from sklearn.preprocessing import RobustScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import davies_bouldin_score

    # Parámetros aleatorios
    n_puntos = np.random.randint(300, 800)
    n_centros = np.random.randint(3, 7)
    ruido = np.random.uniform(0.05, 0.15)

    k_min = 2
    k_max = 10

    # Generar clusters
    X, _ = make_blobs(
        n_samples=n_puntos,
        centers=n_centros,
        cluster_std=0.6,
        random_state=10
    )

    # Outliers
    n_outliers = int(n_puntos * ruido)
    outliers = np.random.uniform(-20, 20, size=(n_outliers, 2))

    X_final = np.vstack([X, outliers])
    np.random.shuffle(X_final)

    # =========================
    # SOLUCIÓN ESPERADA
    # =========================

    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X_final)

    scores = []

    for k in range(k_min, k_max + 1):
        modelo = KMeans(n_clusters=k, random_state=42)

        etiquetas = modelo.fit_predict(X_scaled)

        score = davies_bouldin_score(X_scaled, etiquetas)

        scores.append(score)

    scores = np.array(scores)

    indice_mejor = np.argmin(scores)

    k_optimo = range(k_min, k_max + 1)[indice_mejor]

    score_minimo = round(scores[indice_mejor], 4)

    argumentos = {
        "X": X_final,
        "k_min": k_min,
        "k_max": k_max
    }

    resultado_esperado = (k_optimo, score_minimo)

    return argumentos, resultado_esperado
