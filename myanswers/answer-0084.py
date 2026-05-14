from sklearn.svm import LinearSVC
from sklearn.metrics import average_precision_score

def evaluar_fraude_prauc(X_train, X_test, y_train, y_test):
    # 1. Instanciar el modelo con class_weight='balanced' para manejar el desbalance
    modelo = LinearSVC(class_weight='balanced', random_state=42)
    
    # 2. Entrenar el modelo
    modelo.fit(X_train, y_train)
    
    # 3. Obtener puntajes de confianza continuos (no clases binarias)
    puntajes = modelo.decision_function(X_test)
    
    # 4. Calcular PR-AUC usando average_precision_score
    pr_auc = average_precision_score(y_test, puntajes)
    
    # 5. Retornar diccionario con el modelo y el puntaje
    return {
        'modelo': modelo,
        'pr_auc': pr_auc
    }
