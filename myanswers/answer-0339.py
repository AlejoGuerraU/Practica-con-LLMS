from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def evaluar_modelo_riesgo(df, target_col):
    # 1. Separar X e y
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # 2. Dividir datos 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 3. Entrenar modelo
    modelo = LogisticRegression(random_state=42)
    modelo.fit(X_train, y_train)
    
    # 4. Evaluar el modelo
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # 5. Extraer coeficientes
    coeficientes = modelo.coef_[0]
    
    return (accuracy, coeficientes)
