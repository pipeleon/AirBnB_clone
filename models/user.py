#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Funtion to create a new instance"""
        super().__init__(*args, **kwargs)
