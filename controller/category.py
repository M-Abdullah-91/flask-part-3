from flask import Flask, request
import jwt
from functools import wraps
import query
from controller.user import token_required


def create_category():
    data = request.get_json()

    new_category = query.add_category(data)
    
    return "Added"