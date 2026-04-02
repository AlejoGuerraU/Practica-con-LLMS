import numpy as np
def generar_caso_turbina(n_lecturas=1000):

    np.random.seed(42)
    tiempo = pd.date_range(start="2026-01-01", periods=n_lecturas, freq="10min")
    
    # Temperatura base estable (20°C) con ruido normal
    temp_normal = 20 + np.random.normal(0, 0.5, n_lecturas)
    
    # Inyectar anomalía: En las últimas 200 lecturas la asimetría aumenta
    # y hay picos de calor erráticos (outliers)
    anomalia_idx = range(n_lecturas - 200, n_lecturas)
    for i in anomalia_idx:
        # Generamos una distribución Gamma para forzar asimetría positiva
        temp_normal[i] += np.random.gamma(shape=2.0, scale=1.5) 
    
    df = pd.DataFrame({'temp_ambiente': temp_normal}, index=tiempo)
    
    print(f"--- Simulación de Turbina Generada ---")
    print(f"Total de registros: {n_lecturas}")
    print(f"Periodo de anomalía detectado en el tramo final.")
    
    return df
