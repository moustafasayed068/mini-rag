from helpers.config import get_settings, Settings
import os 

class BaseController:
    
    def __init__(self):
        self.settings = get_settings()
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.file_dire = self.base_path

    def generate_random_string(self, length : int =8):
        import random
        import string
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))