import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# 데이터 만들기 (비 선형 데이터: y = sin(X) + 잡음)
rng = np.random.RandomState(42)
X = np.sort(5 * rng.rand(80, 1), axis=0) # 0~5 사이 숫자 80개를 만들고 정렬
y = np.sin(X).ravel() + 0.1 * rng.randn(80)

print(X)
print(y)

svr = SVR(kernel='rbf', C=10)
svr.fit(X, y)

X_test = np.linspace(0, 5, 200).reshape(-1, 1)
y_pred = svr.predict(X_test)

print(svr.score(X, y))

# 시각화
plt.scatter(X,y, color='darkorange', label='data') # 원래 데이터
plt.plot(X_test, y_pred, color='navv')
