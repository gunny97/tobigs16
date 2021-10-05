from flask import request
from flask import Flask
from flask_cors import CORS # 외부에서 접속해도 에러가 나지 않게 보안 설정 적용
from model import model
import json

# flask instance 생성
app = Flask(__name__)
CORS(app) # 외부에서 접속해도 에러가 나지 않게 보안 설정 적용

""" status check """
# http://localhost:5000/에 접근했을 때, 밑에 index 함수가 실행되어 
# json타입의 형태로 result 딕셔너리를 반환
@app.route("/")
def index():
    result = {
        'message': 'Status is OK.'
    }
    # 파이썬의 객체를 문자열로 변환하기 위하여 json.dumps() 사용
    return json.dumps(result)
    

""" ------------ """

""" model predict """
# http://localhost:5000/predict에 접근했을 때, 메소드를 'POST'형식으로 선언해서, 
# flask에서 메소드 형식을 받아들이며, 밑에 predict_model()함수가 실행되어 json타입의 형태로 result 딕셔너리를 반환
@app.route('/predict', methods=['POST'])
def predict_model():

    print("Predict method Start..")
    #POST 방식으로 들어온 데이터를 파이썬 데이터 형식으로 바꿔줌
    params = request.get_json()
    
    pred = model.predict(params['height'], params['weight'])

    result = {
        'message': 'Succefully Predicted',
        'result': pred
    }

    print("Predict Finish ..")
    print(result)
    # 파이썬의 객체를 문자열로 변환하기 위하여 json.dumps() 사용    
    return json.dumps(result)
""" ------------- """


if __name__ == "__main__":
    app.run();
