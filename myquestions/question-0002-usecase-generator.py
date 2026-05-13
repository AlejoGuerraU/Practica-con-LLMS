def generar_caso_de_uso_financiero(n_muestras=1000):

    import numpy as np

    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_pinball_loss

    np.random.seed(42)

    # ====================================
    # Generación de datos financieros
    # ====================================

    X = np.linspace(0, 10, n_muestras).reshape(-1, 1)

    # Heterocedasticidad
    ruido = np.random.normal(
        0,
        1,
        n_muestras
    ) * (1 + 0.5 * X.flatten())

    y = 2 * X.flatten() + ruido

    cuantil = 0.95

    # ====================================
    # Solución esperada
    # ====================================

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    modelo = GradientBoostingRegressor(
        loss="quantile",
        alpha=cuantil,
        random_state=42
    )

    modelo.fit(X_scaled, y)

    predicciones = modelo.predict(X_scaled)

    pinball = mean_pinball_loss(
        y,
        predicciones,
        alpha=cuantil
    )

    pinball = round(pinball, 4)

    # ====================================
    # Caso de uso
    # ====================================

    argumentos = {
        "X": X,
        "y": y,
        "cuantil": cuantil
    }

    resultado_esperado = {
        "modelo": modelo,
        "predicciones": predicciones,
        "pinball_loss": pinball
    }

    return argumentos, resultado_esperado
