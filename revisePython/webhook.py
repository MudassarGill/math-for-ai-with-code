import requests
user_message='Hi how are you ?'
request_message={'message':user_message}


url="http://localhost:5678/webhook-test/5d159401-26b7-440b-b3bf-e578bdb99714"
response=requests.post(url,json=request_message)
print(response.status_code)