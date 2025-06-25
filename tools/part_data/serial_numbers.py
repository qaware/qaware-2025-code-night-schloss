import random
import string
from datetime import datetime
from enum import Enum

def serial_schema_datecode():
    today = datetime.today().strftime("%Y%m%d")
    rand_suffix = random.randint(1000, 9999)
    return f"SN{today}-{rand_suffix}"


def serial_schema_category():
    categories = ["ENG", "BRK", "TRN", "ELE", "PERF", "DRI", "SUS", "COL"]
    prefix = random.choice(categories)
    mid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    end = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"{prefix}-{mid}-{end}"


def serial_schema_hexblocks():
    def block(): return ''.join(random.choices('0123456789ABCDEF', k=4))

    return f"{block()}-{block()}-{block()}"


def serial_schema_batch():
    year = random.randint(2020, 2025)
    num = random.randint(1, 99999)
    return f"QA-{year}-{num:05d}"


class SerialType(Enum):
    BATCH = "batch"
    HEXBLOCKS = "hexblocks"
    CATEGORY = "category"
    DATECODE = "datecode"

def parse_serial_type(type_str: str) -> SerialType:
    """
    Converts a string to a SerialType enum value.
    Case-insensitive. Raises ValueError if invalid.
    """
    normalized = type_str.strip().lower()
    for serial_type in SerialType:
        if serial_type.value == normalized:
            return serial_type
    raise ValueError(f"Invalid serial type: '{type_str}'. Expected one of: {[t.value for t in SerialType]}")

def generate_serial_by_type(serial_type: SerialType) -> str:
    generators = {
        SerialType.BATCH: serial_schema_batch,
        SerialType.HEXBLOCKS: serial_schema_hexblocks,
        SerialType.CATEGORY: serial_schema_category,
        SerialType.DATECODE: serial_schema_datecode,
    }
    if serial_type in generators:
        return generators[serial_type]()
    else:
        raise ValueError(f"Unknown SerialType: {serial_type}")
