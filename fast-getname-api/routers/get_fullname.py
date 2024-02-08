from fastapi import APIRouter
from pydantic import BaseModel, validator

router = APIRouter()

class User(BaseModel):
    """
    Represents a user with a first name and a last name.
    """
    first_name: str
    last_name: str

    @validator('first_name', 'last_name')
    def validate_name(cls, full_name):
        """
        Validates that the provided name is not empty.
        
        Args:
            full_name (str): The name to validate.
            
        Raises:
            ValueError: If the name is empty.
            
        Returns:
            str: The validated name.
        """
        if not full_name.strip():
            raise ValueError("Name cannot be empty")
        return full_name

@router.post('/api/get_fullname/')
def get_fullname(user: User):
    """
    Concatenates the first name and the last name of the user and returns it.
    
    Args:
        user (User): The user object containing the first and last names.
        
    Returns:
        dict: A dictionary containing the full name.
    """
    full_name = f"{user.first_name} {user.last_name}"
    return {"full_name": full_name}
