import numpy as np
def generar_caso_financiero(n_muestras=1000):

    np.random.seed(42)
    # Variable X: Indicador de volatilidad del mercado
    X = np.linspace(0, 10, n_muestras).reshape(-1, 1)
    
    # El valor del activo (y) tiene ruido que crece proporcionalmente a X
    # Esto crea un "abanico" de incertidumbre.
    ruido = np.random.normal(0, 1, n_muestras) * (1 + 0.5 * X.flatten())
    y = 2 * X.flatten() + ruido
    
    print(f"--- Escenario de Riesgo Generado ---")
    print(f"Simulando {n_muestras} días de operaciones financieras...")
    return X, y

