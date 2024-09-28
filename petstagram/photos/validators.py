from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# def validate_photo_size(value):
#     max_size = 5 * 1024 * 1024
#
#     if value.size > max_size:
#         raise ValidationError(f"Image file too large ( > 5MB ). Please upload a smaller file.")
#

@deconstructible
class PhotoSizeValidator:
    def __init__(self, file_size_mb, message=None):
        self.file_size_in_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File must be below ot equal to {self.file_size_in_mb} MB."
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.file_size_in_mb * 1024 * 1024:
            raise ValidationError(self.message)
