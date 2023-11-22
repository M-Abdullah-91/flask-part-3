from flask import Flask, request
import jwt
from functools import wraps
import query

secret_key = "THISISSECRETKEY"

def token_required(func):
    @wraps(func)
    def token_required(*args,**kwargs):
        token = request.headers.get("Authorization")
        
        if token is None or len(token) <= 0:
            return { "ERROR": "Token Required "}, 400
        
        decoded_token=jwt.decode(
            token, 
            secret_key, 
            algorithms="HS256"
        )
       
        response =  func(decoded_token, *args, *kwargs)

        return response
        
    return token_required


def register():
    data = request.get_json()
    
    if data is None:
        return {"ERROR":"field are required"}
    
    register = query.register(data)
    if register is None:
        return {"ERROR": "Registration failed"}, 400
    
    return "Registered Successfully"

    

def login():
    data = request.get_json()

    if data is None:
        return {"ERROR":"fields are missing"},400
    
    user_data = query.login(data)

    token_data = {
        'id':user_data['id'],
        'email': user_data['email'],
        'password': user_data['password']
    }

    token  = jwt.encode(token_data,secret_key,algorithm="HS256")
    
    
    return token,200
