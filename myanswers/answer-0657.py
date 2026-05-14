import pandas as pd
import numpy as np

def ingresos_por_categoria(df_ventas, df_catalogo):
    # 1. Merge con inner join
    df_merged = pd.merge(df_ventas, df_catalogo, on='id_producto', how='inner')
    
    # 2. Nueva columna ingreso_total
    df_merged['ingreso_total'] = df_merged['cantidad_vendida'] * df_merged['precio_unitario']
    
    # 3. Agrupar por categoria y sumar
    df_grouped = df_merged.groupby('categoria_producto')['ingreso_total'].sum()
    
    # 4. Ordenar de mayor a menor
    df_sorted = df_grouped.sort_values(ascending=False)
    
    # 5. Retornar como array numpy
    return df_sorted.values
