import json


def export_category_report(totals, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(totals, file, indent=4)

    print("Category report exported successfully!")