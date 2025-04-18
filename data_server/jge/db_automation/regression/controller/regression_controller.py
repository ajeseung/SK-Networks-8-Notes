from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# pip install scikit-learn

class RegressionController(viewsets.ViewSet):

    # postman -> http://localhost:8000/regression/request-logistic-regression
    def requestLogisticRegression(self, request):
        print(f"데이터 준비")
        iris = load_iris()
        # 특성
        X = iris.data
        # 레이블
        y = iris.target

        print(f"Features: {iris.feature_names}")
        print(f"Labels: {iris.target_names}")

        # 이진 분류를 사용하도록 실제 구성에서 2번째에 해당하는 부분을 배제함
        X = X[y != 2]
        y = y[y != 2]

        # 훈련 데이터와 테스트 데이터 분류
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # 로지스틱 회귀 모델 생성
        model = LogisticRegression()
        # 모델 훈련
        model.fit(X_train, y_train)
        # 예측
        y_pred = model.predict(X_test)
        # 정확도 평가
        accuracy = accuracy_score(y_test, y_pred)
        print(f"accuracy: {accuracy:.4f}")
        # 혼동 행렬
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(f"confusion matrix: {conf_matrix}")

        responseData = {
            "accuracy": round(accuracy, 4),
            "confusion_matrix": conf_matrix.tolist()
        }

        return JsonResponse(responseData, status=status.HTTP_200_OK)
