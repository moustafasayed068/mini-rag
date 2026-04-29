import re
import os
from .BaseController import BaseController
from .ProjectController import ProjectController
from  fastapi import UploadFile
from models import ResponseEnum

class DataController(BaseController):

    def __init__(self):
        super().__init__()
        self.file_size_scaled = 1048576 * self.settings.FILE_MAX_SIZE

    def validate_file(self, file: UploadFile):

        if file.content_type not in self.settings.FILE_EXTENSIONS:
            return False, ResponseEnum.bad_file_type 
        
        if file.size > self.file_size_scaled:
            return False, ResponseEnum.file_too_large
        
        return True, ResponseEnum.file_valid
    def generate_filename(self, original_filename: str, project_id: str):
        random_string = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        cleaned_filename = self.clean_original_filename(original_filename=original_filename)
        new_file_path = os.path.join(project_path, f"{random_string}_{cleaned_filename}")

        while os.path.exists(new_file_path):
            random_string = self.generate_random_string()
            new_file_path = os.path.join(project_path, f"{random_string}_{cleaned_filename}")
        return new_file_path

    def clean_original_filename(self, original_filename: str):
        cleaned_filename = re.sub(r'[^\w.]', '', original_filename)
        cleaned_filename = cleaned_filename.replace(' ', '_')
        return cleaned_filename
