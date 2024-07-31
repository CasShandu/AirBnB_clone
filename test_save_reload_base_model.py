#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import os

# Clear old data before the test
file_path = "file.json"
if os.path.exists(file_path):
    os.remove(file_path)

# Reload all objects from storage
print("-- Reloaded objects --")
all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create and save a new object
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

# Reload and print objects again
print("-- Reloaded objects after saving new object --")
all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

