#!/usr/bin/python3
"""class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Funtion to create a new instance"""
        super().__init__(*args, **kwargs)
