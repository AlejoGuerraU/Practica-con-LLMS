def ingresos_por_categoria(df_ventas, df_catalogo):
    # 1. Fusionar los DataFrames usando inner join
    df_merged = pd.merge(
        df_ventas,
        df_catalogo,
        on='id_producto',
        how='inner'
    )

    # 2. Crear la columna ingreso_total
    df_merged['ingreso_total'] = (
        df_merged['cantidad_vendida'] *
        df_merged['precio_unitario']
    )

    # 3. Agrupar por categoria y sumar ingresos
    agrupado = (
        df_merged
        .groupby('categoria_producto')['ingreso_total']
        .sum()
    )

    # 4. Ordenar de mayor a menor
    agrupado = agrupado.sort_values(ascending=False)

    # 5. Retornar como arreglo de numpy
    return agrupado.values
