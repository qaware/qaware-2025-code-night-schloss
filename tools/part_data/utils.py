import random
import string
from datetime import datetime, timedelta

from part_data.serial_numbers import generate_serial_by_type, parse_serial_type

# Define named styles
STYLE_GENERATORS = {
    "uppercase_2": lambda: ''.join(random.choices(string.ascii_uppercase, k=2)),  # e.g., "RS"
    "digits_3": lambda: ''.join(random.choices(string.digits, k=3)),  # e.g., "720"
    "mixed_3": lambda: ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)),  # e.g., "F7Q"
    "letter_digit": lambda: random.choice(string.ascii_uppercase) + str(random.randint(1, 99))  # e.g., "X9"
}


def generate_suffix_or_prefix(style=None):
    """
    Generate a random tag for prefix or suffix based on a given style.
    If style is None, choose one at random.
    """
    if style:
        generator = STYLE_GENERATORS.get(style)
        if not generator:
            raise ValueError(f"Invalid style '{style}'. Available styles: {list(STYLE_GENERATORS.keys())}")
    else:
        generator = random.choice(list(STYLE_GENERATORS.values()))
    return generator()


def augment_product_name(name, style=None, position=None):
    """
    Add a prefix or suffix to a product name using a specified or random style.

    Args:
        name (str): The base product name.
        style (str, optional): Style name for tag ('uppercase_2', 'digits_3', 'mixed_3', 'letter_digit').
        position (str, optional): 'prefix', 'suffix', or None for random.

    Returns:
        str: Augmented product name.
    """
    tag = generate_suffix_or_prefix(style)
    if position == 'prefix':
        return f"{tag} {name}"
    elif position == 'suffix':
        return f"{name} {tag}"
    else:
        return f"{tag} {name}" if random.choice([True, False]) else f"{name} {tag}"


def generate_random_production_date(start_year=2015, end_year=2025):
    """
    Generates a random production date string in 'YYYY-MM-DD' format.

    Args:
        start_year (int): Earliest possible year (inclusive).
        end_year (int): Latest possible year (inclusive).

    Returns:
        str: Random date like '2023-11-15'
    """
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")


def list_categories(parts):
    """
    Extracts and returns a sorted list of unique categories from the parts data.
    """
    categories = set()
    for part in parts:
        category = part.get("Category")
        if category:  # Ignore None or empty
            categories.add(category.strip())
    return sorted(categories)


def filter_by_category(parts, category):
    """
    Filters the parts list by category.
    """
    return [part for part in parts if part['Category'].lower() == category.lower()]


def get_random_element(data: list) -> str:
    return data[random.randint(0, len(data) - 1)]


def extract_uppercase_letters(text):
    """
    Returns a string containing only the uppercase letters from the input.

    Args:
        text (str): The input string.

    Returns:
        str: A string of uppercase characters.
    """
    return ''.join(char for char in text if char.isupper())


def random_compatible_brands(min_items=1, max_items=5):
    """
    Returns a random sublist of car brands.

    Args:
        min_items (int): Minimum number of brands to include.
        max_items (int): Maximum number of brands to include.

    Returns:
        list: Random selection of compatible brands.
    """
    brands = [
        "BMV",
        "WV",
        "Nord",
        "Feramborghini",
        "Mecentley"
    ]
    sample_size = random.randint(min_items, min(max_items, len(brands)))
    return random.sample(brands, sample_size)

def generate_random_price(min_price=10.0, max_price=2000.0, decimals=2):
    """
    Generates a random float price between min_price and max_price.
    """
    return round(random.uniform(min_price, max_price), decimals)

def generate_random_flag(true_prob=0.8):
    """
    Returns True or False, with a default 80% chance of being True.
    """
    return random.random() < true_prob

def generate_random_currency():
    """
    Randomly selects a currency code.
    """
    currencies = ["EUR", "USD", "GBP", "JPY", "CHF"]
    return random.choice(currencies)


def generate_random_flags(min_flags=1, max_flags=8):
    """
    Returns a random list of flag names (as strings) from a predefined set.

    Args:
        min_flags (int): Minimum number of flags to include.
        max_flags (int): Maximum number of flags to include.

    Returns:
        list[str]: A list of randomly selected flag names.
    """
    all_flags = [
        "used",
        "refurbished",
        "limitedEdition",
        "requiresCalibration",
        "recalled",
        "oemPart",
        "aftermarket",
        "ecoFriendly",
        "obsolete",
        "digitallyTracked",
        "hazardousMaterial",
        "customFabricated",
        "safetyCritical"
    ]

    count = random.randint(min_flags, min(max_flags, len(all_flags)))
    return random.sample(all_flags, count)

def snake_to_camel(snake_str):
    """
    Converts a snake_case string to camelCase.

    Example: 'production_date' -> 'productionDate'
    """
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def format(attribute_name, format = None):
    if format == "upper":
        return attribute_name.upper()
    elif format == "camel":
        return snake_to_camel(attribute_name)
    else:
        return attribute_name

def random_parts_for_category(category, all_parts, producer, currency, flags):
    random_parts = []

    serial_type = parse_serial_type(producer.get("serialType"))
    producer_prefix = extract_uppercase_letters(producer.get("name"))
    parts_for_category = filter_by_category(all_parts, category)

    parts_count = random.randint((len(parts_for_category) // 3), len(parts_for_category) * 5)

    part_name_style = producer.get("partNameStyle")
    part_name_position = producer.get("partNamePosition")
    format_type = producer.get("attributeNameFormat")

    for idx in range(parts_count):
        random_part = {}

        part = get_random_element(parts_for_category)

        random_part[format("category", format_type)] = category
        random_part[format("name", format_type)] = augment_product_name(part.get("Part"), part_name_style, part_name_position)
        random_part[format("description", format_type)] = part.get("Description")
        random_part[format("serial", format_type)] = producer_prefix + "-" + generate_serial_by_type(serial_type)
        random_part[format("production_date", format_type)] = generate_random_production_date()
        random_part[format("price", format_type)] = generate_random_price()
        random_part[format("currency", format_type)] = currency
        random_part[format("authorised", format_type)] = generate_random_flag()
        random_part[format("in_stock", format_type)] = generate_random_flag()
        random_part[format("compatible_brands", format_type)] = random_compatible_brands()
        for flag in flags:
           random_part[format(flag, format_type)] = generate_random_flag(0.6)

        random_parts.append(random_part)

    return random_parts
