import numpy as np
import pandas as pd

def generar_caso_de_uso_turbina(n_lecturas=1000):

    np.random.seed(42)
    tiempo = pd.date_range(start="2026-01-01", periods=n_lecturas, freq="10min")
    
    # Temperatura base estable (20°C) con ruido normal
    temp_normal = 20 + np.random.normal(0, 0.5, n_lecturas)
    
    # Inyectar anomalía en las últimas lecturas
    anomalia_idx = range(n_lecturas - 200, n_lecturas)

    for i in anomalia_idx:
        temp_normal[i] += np.random.gamma(shape=2.0, scale=1.5)

    df = pd.DataFrame(
        {"temp_ambiente": temp_normal},
        index=tiempo
    )
    
    print("--- Simulación de Turbina Generada ---")
    print(f"Total de registros: {n_lecturas}")
    print("Periodo de anomalía detectado en el tramo final.")
    
    return df, {"col_sensor": "temp_ambiente", "ventana": 12}
