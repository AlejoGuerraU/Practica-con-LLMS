def evaluar_modelo_riesgo(df, target_col):
    # 1. Separar variables predictoras (X) y objetivo (y)
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 2. Dividir datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # 3. Crear y entrenar el modelo
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # 4. Realizar predicciones
    y_pred = model.predict(X_test)

    # 5. Calcular accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # 6. Obtener coeficientes
    coeficientes = model.coef_

    # 7. Retornar resultados
    return (accuracy, coeficientes)
