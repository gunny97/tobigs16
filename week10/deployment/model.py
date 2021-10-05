from joblib import load
import numpy as np

#bmiRegressor 모델 불러오기
model = load('./model/model_params/bmiRegressor')

#불러온 모델을 활용해서 int형식으로 받은 height와 weight를 사용해서 bmi예측
def predict(height: int, weight: int):
    print("Model Start")
    result = model.predict([[height, weight]])
    print("Model Finish")
    return result.item()