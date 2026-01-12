from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def train(X, y):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    dump(model, "model/saved_model.pkl")
    return model
