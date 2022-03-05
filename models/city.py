#!/usr/bin/python3
"""class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Funtion to create a new instance"""
        super().__init__(*args, **kwargs)
