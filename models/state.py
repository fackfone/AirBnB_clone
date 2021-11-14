#!/usr/bin/python3
"""
This module defines the State class herited from BaseModel
"""

from models.base_model import BaseModel
import json


class State(BaseModel):

    """State class for Airbnb clone project"""
    name = ""
