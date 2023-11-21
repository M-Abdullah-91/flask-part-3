from flask import Flask, request
import jwt
from functools import wraps
import query

secret_key = "THISISSECRETKEY"

def token_required(func):
    @wraps(func)
    def token_required(*args,**kwargs):
        token = request.args.get("token")
        
        if token is None or len(token) <= 0:
            return { "ERROR": "Token Required "}, 400
        
        user=jwt.decode(
            token, 
            secret_key, 
            algorithms="HS256"
        )
       
        response =  func(user, *args, *kwargs)

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

    