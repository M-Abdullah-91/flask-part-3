from flask import Flask, request
import jwt
from functools import wraps
import query
from controller.user import token_required


@token_required
def create_notes(data):
    data = request.get_json()

    if data is None:
        return {"ERROR":"fields are missing"}   

    # new_note = query.add_notes(data)
    new_note = query.add_notes(data)

    return "New Note Added "

@token_required
def assign_note_category(data):
    data = request.get_json()

    if data is None:
        return {"ERROR":"fields are missing"}   
    
    assign_note = query.assign_note_category(data)

    return "Assigned"


@token_required
def view_notes(data): 
    notes= query.view_notes()
    if notes is None:
        return {"NO NOTES"} 
    
    return notes,200



def get_notes_by_category():
    data = request.get_json()
    
    notes_by_category = query.get_notes_by_category(data)

    if notes_by_category is None:
        return {"NO NOTES"} 
    
    return notes_by_category,200



