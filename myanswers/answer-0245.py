def limpiar_leads_marketing(df):
    # 1. Calcular el umbral del 50%
    umbral = len(df) * 0.5

    # 2. Conservar solo columnas con <= 50% de nulos
    cols_validas = df.columns[df.isnull().sum() <= umbral]

    # 3. Filtrar columnas válidas
    df_limpio = df[cols_validas]

    # 4. Eliminar duplicados
    df_limpio = df_limpio.drop_duplicates()

    # 5. Eliminar filas con nulos
    df_limpio = df_limpio.dropna()

    # 6. Reiniciar índices
    df_limpio = df_limpio.reset_index(drop=True)

    # 7. Retornar DataFrame limpio
    return df_limpio
