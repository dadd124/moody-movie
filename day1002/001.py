# 타이타닉 데이터 분류 모델 학습/평가 예제

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, RocCurveDisplay

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


# ================================
# 1. 데이터 불러오기 및 전처리
# ================================
titanic = sns.load_dataset("titanic")   # seaborn 내장 Titanic 데이터셋
print(titanic.head())

# 주요 변수 선택
data = titanic[["survived", "pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]]

# 결측치 처리
data = data.dropna()

# 범주형 -> 수치형 변환
data = pd.get_dummies(data, columns=["sex", "embarked"], drop_first=True)

# X, y 분리
X = data.drop("survived", axis=1)
y = data["survived"]

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 스케일링 (로지스틱 회귀용)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ================================
# 2. 모델 정의 및 그리드 서치
# ================================
# (1) Logistic Regression
param_grid_lr = {
    "C": [0.01, 0.1, 1, 10],
    "solver": ["liblinear", "lbfgs"]
}

grid_lr = GridSearchCV(LogisticRegression(max_iter=1000), param_grid_lr,
                       cv=5, scoring="accuracy")
grid_lr.fit(X_train_scaled, y_train)

print("Best Logistic Regression Params:", grid_lr.best_params_)
print("Best LR Score:", grid_lr.best_score_)

# (2) Random Forest
param_grid_rf = {
    "n_estimators": [100, 200],
    "max_depth": [3, 5, None],
    "min_samples_split": [2, 5]
}

grid_rf = GridSearchCV(RandomForestClassifier(random_state=42),
                       param_grid_rf, cv=5, scoring="accuracy")
grid_rf.fit(X_train, y_train)

print("Best RandomForest Params:", grid_rf.best_params_)
print("Best RF Score:", grid_rf.best_score_)


# ================================
# 3. 최종 성능 평가
# ================================
models = {
    "Logistic Regression": grid_lr.best_estimator_,
    "Random Forest": grid_rf.best_estimator_
}

for name, model in models.items():
    if name == "Logistic Regression":
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
    else:
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

    print(f"\n=== {name} ===")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.3f})")

# ================================
# 4. ROC Curve 시각화
# ================================
plt.plot([0,1],[0,1],'k--')  # 기준선
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
