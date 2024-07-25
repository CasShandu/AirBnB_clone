#!/user/bin/python3

from datetime import datetime
import uuid
import json

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
        if kwargs:
            valid_keys = {'id', 'created_at', 'updated_at'}
            for key in kwargs:
                if key == '__class__':
                    continue  # Ignore __class__ key
                if key not in valid_keys:
                    raise TypeError(f"Unexpected keyword argument '{key}'")
            
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid.uuid4())
            
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = self.created_at
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates updated_at attribute with current datetime and simulates saving object state.
        """
        self.updated_at = datetime.now()
        # Simulate saving state to file.json (for testing purposes)
        with open('file.json', 'w') as f:
            json.dump({f"{self.__class__.__name__}.{self.id}": self.to_dict()}, f)

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
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

