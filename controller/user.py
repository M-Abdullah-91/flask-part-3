from flask import request
import jwt
from functools import wraps

secret_key = "THISISSECRETKEY"

def token_required(func):
    @wraps(func)
    def token_required(*args,**kwargs):
        token = request.args.get("token")
        
        user=jwt.decode(
            token, 
            secret_key, 
            algorithms="HS256"
        )
       
        response =  func(user, *args, *kwargs)

        return response
        
    return token_required

