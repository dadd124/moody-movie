import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
print(df)
print()
df.info()

'''

붓꽃 데이터
1936년 논문에서 처음 사용
영국의 통계학자가 통계적 분류 기법을 설명하기 위해 만든 예제 데이터
총 150개 샘플

꽃받침 길이 (sepal length, cm)
꽃받침 너비 (sepal width, cm)
꽃잎 길이 (petal length, cm)
꽃잎 너비 (petal width, cm)

Setosa (세토사) -> 작고 단순한 꽃, 다른 두 종과 확실히 구분 가능
Versicolor (버시컬러) -> 중간크기, 특징이 섞여있음
Virginica (버지니카) -> 가장 크고 구분이 까다로움
'''

sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species")
plt.show()

# 훈련데이터 준비 >>>> 입력(X), 타깃(Y)
X = df.drop("species", axis=1)
y = df["species"]

# 훈련/테스트 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=16)

# 최근접이웃 3이웃으로 knn 변수명에 불러오기

kn = KNeighborsClassifier(n_neighbors=3)

# 불러와서 학습 시키기

kn.fit(X_train, y_train)

# 테시트셋 예측 시켜서 y_pred 에 담기

y_pred = kn.predict(X_test)

print('예측값: ', y_pred)
print('실제값: ', y_test)
print('트레인 스코어: ', kn.score(X_train, y_train))
print('테스트 스코어: ', kn.score(X_test, y_test))

from sklearn.metrics import accuracy_score

print('정확도: ', accuracy_score(y_test, y_pred))
# 스코어랑 같은 결과다. 단, 트레인 스코어는 값이 약간 다를 수 있음.

