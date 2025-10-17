import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import numpy as np
import seaborn as sns


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset('titanic')

data = titanic[["survived", "pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]]
data = data.dropna()
data = pd.get_dummies(data, columns=["sex", "embarked"], drop_first=True)

X = data.drop("survived", axis=1)
y = data["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid_lr = {
    "C": [0.01, 0.1, 1, 10],
    "solver": ["liblinear", "lbfgs"]
}
grid_lr = GridSearchCV(LogisticRegression(max_iter=1000), param_grid_lr, cv=5, scoring="accuracy")
grid_lr.fit(X_train_scaled, y_train)

param_grid_rf = {
    "n_estimators": [100, 200],
    "max_depth": [3, 5, None],
    "min_samples_split": [2, 5]
}
grid_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring="accuracy")
grid_rf.fit(X_train, y_train)

models = {
    "로지스틱 회귀": grid_lr.best_estimator_,
    "랜덤 포레스트": grid_rf.best_estimator_
}

from sklearn.metrics import accuracy_score, roc_curve, auc

for name, model in models.items():
    if name == "Logistic Regression":
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
    else:
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]    
    
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} 정확도(Accuracy): {acc:.3f}")

    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.3f})")

plt.plot([0,1],[0,1],'k--') 
plt.xlabel("거짓 양성")
plt.ylabel("민감도")
plt.title("ROC 곡선")
plt.legend()
plt.show()