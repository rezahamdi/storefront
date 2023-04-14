from django.core.exceptions import ValidationError

def validate_file_size(file):
    file_max_length = 100
    if file.size > file_max_length *1024:
        raise ValidationError(f'file size cannot be grater than{file_max_length}KB!')