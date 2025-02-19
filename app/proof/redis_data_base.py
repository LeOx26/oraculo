import redis
import auht
import numpy as np
import json

global dataBase

dataBase=redis.Redis(host="localhost", port=6379, db=0)

def create_table():