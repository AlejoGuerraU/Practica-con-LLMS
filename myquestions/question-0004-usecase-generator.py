def generar_caso_de_uso_ecommerce(n_usuarios=400):

    import numpy as np
    import pandas as pd

    from sklearn.manifold import TSNE
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.metrics import silhouette_score

    np.random.seed(42)
    data = np.random.rand(n_usuarios, 10)

    # Inyección de infinitos
    mask_inf = np.random.choice(
        [True, False],
        size=data.shape,
        p=[0.05, 0.95]
    )

    data[mask_inf] = np.inf

    # Inyección de NaN
    mask_nan = np.random.choice(
        [True, False],
        size=data.shape,
        p=[0.05, 0.95]
    )

    data[mask_nan] = np.nan

    columnas = [
        f"metrica_{i}"
        for i in range(10)
    ]

    df = pd.DataFrame(
        data,
        columns=columnas
    )

    n_clusters = 3

    # ====================================
    # Solución esperada
    # ====================================

    df_limpio = df.copy()

    # Reemplazar infinitos
    for col in df_limpio.columns:

        maximo_columna = (
            df_limpio.loc[
                ~np.isinf(df_limpio[col]),
                col
            ].max()
        )

        df_limpio[col] = np.where(
            np.isinf(df_limpio[col]),
            maximo_columna,
            df_limpio[col]
        )

    # Completar NaN con mediana
    for col in df_limpio.columns:

        mediana = df_limpio[col].median()

        df_limpio[col] = (
            df_limpio[col]
            .fillna(mediana)
        )

    tsne = TSNE(
        n_components=2,
        random_state=42
    )

    X_tsne = tsne.fit_transform(df_limpio)

    clustering = AgglomerativeClustering(
        n_clusters=n_clusters
    )

    labels = clustering.fit_predict(X_tsne)

    score = silhouette_score(
        X_tsne,
        labels
    )

    score = round(score, 4)

    resultado = df.copy()

    resultado["subsegmento_id"] = labels

    argumentos = {
        "df": df,
        "n_clusters": n_clusters
    }

    resultado_esperado = (
        resultado,
        score
    )

    return argumentos, resultado_esperado
