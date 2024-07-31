#!/usr/bin/python3

from datetime import datetime
import uuid
import models

class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Public instance attributes:
        id: string - Unique identifier generated using uuid.uuid4().
        created_at: datetime - Timestamp when instance is created.
        updated_at: datetime - Timestamp updated whenever object is modified.

    Public instance methods:
        save(self): Updates updated_at with current datetime and simulates persisting state.
        to_dict(self): Returns dictionary representation of instance attributes.
        __str__(self): Returns string representation of the instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            TypeError: If kwargs contain unexpected or invalid keys.
        """

class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        
        models.storage.new(self)


    def save(self):
        """
        Updates updated_at attribute with current datetime and simulates saving object state.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of instance attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

if __name__ =="__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
