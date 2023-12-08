import uuid
import posixpath
from datetime import datetime

from django.core.files.utils import validate_file_name
from django.db import models


def _generate_filename(inst_upload_to, filename) -> str:
    ext = filename.split('.')[-1]
    hash_name = str(uuid.uuid4())
    filename = f"{hash_name}.{ext}"
    upload_to = f"{inst_upload_to}/%Y/%m/%d/"
    dirname = datetime.now().strftime(upload_to)
    filename = posixpath.join(dirname, filename)
    filename = validate_file_name(filename, allow_relative_path=True)
    return filename


class FileField(models.FileField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


class ImageField(models.ImageField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))
