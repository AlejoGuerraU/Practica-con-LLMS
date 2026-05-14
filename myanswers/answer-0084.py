def evaluar_fraude_prauc(X_train, X_test, y_train, y_test):
    # 1. Crear el modelo SVM lineal
    modelo = LinearSVC(
        class_weight='balanced',
        random_state=42,
        max_iter=2000
    )

    # 2. Entrenar el modelo
    modelo.fit(X_train, y_train)

    # 3. Obtener scores continuos
    y_scores = modelo.decision_function(X_test)

    # 4. Calcular PR-AUC
    pr_auc = average_precision_score(y_test, y_scores)

    # 5. Retornar resultados
    return {
        'modelo': modelo,
        'pr_auc': pr_auc
    }
