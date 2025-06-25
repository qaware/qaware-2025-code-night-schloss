import os

from part_data.parsers import parse_csv, parse_producers_json
from part_data.utils import random_parts_for_category, generate_random_flags
from part_data.writers import write_dict_list_to_csv, write_dict_list_to_json, write_dict_list_to_txt
from part_data.utils import generate_random_currency

if __name__ == "__main__":
    all_parts = parse_csv("tools/part_data/parts.csv")
    producers = parse_producers_json("tools/part_data/producers.json")

    for producer in producers:
        parts_for_producer = []

        currency = generate_random_currency()

        flags = generate_random_flags()

        filename = "hersteller_daten/" + producer.get("name").replace(" ", "_").replace(".", "")

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        for category in producer.get("categories"):
            parts_for_producer.extend(random_parts_for_category(category, all_parts, producer, currency, flags))

        if producer.get("format") == "csv":
            write_dict_list_to_csv(parts_for_producer, filename + ".csv")
        elif producer.get("format") == "json":
            write_dict_list_to_json(parts_for_producer, filename + ".json")
        elif producer.get("format") == "txt":
            write_dict_list_to_txt(parts_for_producer, filename + ".txt")
        else:
            print(f"Unknown format {producer.get('format')}")
