#!/usr/bin/python3
"""class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Funtion to create a new instance"""
        super().__init__(*args, **kwargs)
