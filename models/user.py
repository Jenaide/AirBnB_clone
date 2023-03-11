#!/usr/bin/python3
"""
Created by
@author: Jenaide Sibolie
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel
    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
