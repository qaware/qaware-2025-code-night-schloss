import csv
import json
def parse_csv(filepath):
    """
    Parses a car parts CSV file into a list of dictionaries.
    Each dictionary represents one part.
    """
    parts = []
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                parts.append({
                    "Part": (row.get("Part") or "").strip(),
                    "Category": (row.get("Category") or "").strip(),
                    "Description": (row.get("Description") or "").strip()
                })
        print(f"Successfully parsed {len(parts)} parts from {filepath}")
        return parts
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        return []


def parse_producers_json(filepath):
    """
    Parses a JSON file of car part producers into a list of dictionaries.
    Each dictionary contains 'name', 'description', and 'categories'.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                print(f"Successfully parsed {len(data)} producers.")
                return data
            else:
                print("Invalid JSON format: Expected a list.")
                return []
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
