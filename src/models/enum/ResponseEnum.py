from enum import Enum

class ResponseEnum(Enum):
    
    SUCCESS = "success"
    ERROR = "error"
    bad_file_type = "Invalid file type"
    file_too_large = "File size exceeds the maximum limit"
    file_valid = "File is valid"

