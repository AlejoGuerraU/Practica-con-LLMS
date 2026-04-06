import numpy as np
import pandas as pd
def generar_caso_de_uso_ecommerce(n_usuarios=400):

    np.random.seed(42)
    # Creamos 10 variables (clics, scroll, tiempo, etc.)
    data = np.random.rand(n_usuarios, 10)
    
    # Inyectar errores de sensores (Infinitos y NaNs)
    # 5% de los datos serán infinitos por errores de división en frontend
    mask_inf = np.random.choice([True, False], size=data.shape, p=[0.05, 0.95])
    data[mask_inf] = np.inf
    
    # 5% de los datos serán nulos
    mask_nan = np.random.choice([True, False], size=data.shape, p=[0.05, 0.95])
    data[mask_nan] = np.nan
    
    columnas = [f'metrica_{i}' for i in range(10)]
    df = pd.DataFrame(data, columns=columnas)
    
    print(f"--- Dataset de Navegación E-commerce Generado ---")
    print(f"Dimensiones: {df.shape}")
    print(f"Sensores con errores detectados (inf/nan)... listo.")
    
    return {"df": df}, {"n_clusters": 4}
