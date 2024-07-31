#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

def test_save_reload():
    """Test saving and reloading of BaseModel instances."""
    
    # Print all currently stored objects
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id, obj in all_objs.items():
        print(obj)

    # Create and save a new object
    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)

    # Print all objects after saving the new one
    all_objs = storage.all()
    print("-- Objects after saving new instance --")
    for obj_id, obj in all_objs.items():
        print(obj)

    # Reload objects from storage to confirm persistence
    print("-- Reload objects after reloading from file --")
    storage.reload()
    all_objs = storage.all()
    for obj_id, obj in all_objs.items():
        print(obj)

if __name__ == "__main__":
    test_save_reload()

