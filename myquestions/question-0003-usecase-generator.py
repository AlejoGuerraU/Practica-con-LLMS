def generar_caso_de_uso_turbina(n_lecturas=1000):

    import numpy as np
    import pandas as pd

    from sklearn.preprocessing import RobustScaler

    np.random.seed(42)

    # ====================================
    # Generación de serie temporal
    # ====================================

    tiempo = pd.date_range(
        start="2026-01-01",
        periods=n_lecturas,
        freq="10min"
    )

    # Temperatura estable
    temp_normal = 20 + np.random.normal(
        0,
        0.5,
        n_lecturas
    )

    # Anomalías térmicas
    anomalia_idx = range(
        n_lecturas - 200,
        n_lecturas
    )

    for i in anomalia_idx:
        temp_normal[i] += np.random.gamma(
            shape=2.0,
            scale=1.5
        )

    df = pd.DataFrame(
        {"temp_ambiente": temp_normal},
        index=tiempo
    )

    col_sensor = "temp_ambiente"

    ventana = 12

    # ====================================
    # Solución esperada
    # ====================================

    resultado = pd.DataFrame(index=df.index)

    # Asimetría móvil
    resultado["asimetria_movil"] = (
        df[col_sensor]
        .rolling(window=ventana)
        .skew()
    )

    # Rango móvil
    resultado["rango_movil"] = (
        df[col_sensor]
        .rolling(window=ventana)
        .max()
        -
        df[col_sensor]
        .rolling(window=ventana)
        .min()
    )

    # Tasa de cambio
    resultado["tasa_cambio"] = (
        df[col_sensor]
        .diff()
    )

    # Eliminar NaN
    resultado = resultado.dropna()

    # Escalado robusto
    scaler = RobustScaler()

    columnas = [
        "asimetria_movil",
        "rango_movil",
        "tasa_cambio"
    ]

    resultado[columnas] = scaler.fit_transform(
        resultado[columnas]
    )

    # ====================================
    # Caso de uso
    # ====================================

    argumentos = {
        "df": df,
        "col_sensor": col_sensor,
        "ventana": ventana
    }

    resultado_esperado = resultado

    return argumentos, resultado_esperado
