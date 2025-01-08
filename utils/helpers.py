import time
from pathlib import Path


def append_zeros(val):
    count = len(str(val))
    diff = 6 - count
    name_val = str(val)
    if diff > 0:
        name_val = "0"
        for i in range(diff - 1):
            name_val = name_val + "0"
        name_val = name_val + str(val)
    return name_val


def create_storage_filename(file_type, file_name):
    extension = Path(file_name).suffix
    if not extension:
        raise ValueError("Unable to determine file extension")
    timestamp = int(time.time())  # Unix timestamp
    filename = f"{file_type}_{timestamp}{extension}"
    return filename
