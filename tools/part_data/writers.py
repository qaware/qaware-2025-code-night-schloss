import csv
import json


# def write_dict_list_to_csv(dict_list, filepath):
#     """
#     Writes a list of dictionaries to a CSV file.
#     - Each dictionary becomes a row.
#     - Keys of the first dictionary define the column headers.
#
#     Args:
#         dict_list (list): List of dictionaries with uniform keys.
#         filepath (str): Path to save the CSV file.
#     """
#     if not dict_list:
#         raise ValueError("The dictionary list is empty.")
#
#     # Extract column headers from the first item
#     headers = dict_list[0].keys()
#
#     with open(filepath, mode='w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(dict_list)
#
#     print(f"CSV written successfully to: {filepath}")


def write_dict_list_to_csv(dict_list, filepath):
    """
    Writes a list of dictionaries to a CSV file.
    Converts list values (e.g., categories) to comma-separated strings.
    """
    if not dict_list:
        raise ValueError("The dictionary list is empty.")

    headers = dict_list[0].keys()

    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in dict_list:
            row_serialized = {
                k: ','.join(v) if isinstance(v, list) else v
                for k, v in row.items()
            }
            writer.writerow(row_serialized)

    print(f"CSV written successfully to: {filepath}")

def write_dict_list_to_json(data, filepath, indent=2):
    """
    Writes a list of dictionaries (or a single dictionary) to a JSON file.

    Args:
        data (list or dict): The data to write (usually a list of dicts).
        filepath (str): Path to save the JSON file.
        indent (int): Indentation level for pretty-printing (default: 2).
    """
    if not data:
        raise ValueError("The data is empty and cannot be written to JSON.")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

    print(f"JSON written successfully to: {filepath}")


def write_dict_list_to_txt(dict_list, filepath):
    """
    Writes a list of dictionaries to a custom TXT format.
    Converts lists to comma-separated strings instead of brackets.
    """
    if not dict_list:
        raise ValueError("The dictionary list is empty.")

    with open(filepath, 'w', encoding='utf-8') as f:
        for item in dict_list:
            f.write("%%BEGIN_ITEM%%\n")
            for key, value in item.items():
                if isinstance(value, list):
                    value_str = ','.join(map(str, value))
                else:
                    value_str = str(value)
                f.write(f"::{key}:: {value_str}\n")
            f.write("%%END_ITEM%%\n\n")

    print(f"TXT file written successfully to: {filepath}")
