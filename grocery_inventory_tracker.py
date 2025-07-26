def track_inventory():
    import json
    import os
    json_file = "inventory_data.json"

    # Load existing inventory from JSON file if it exists
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            data = json.load(f)
            inventory = data.get("inventory", {})
    else:
        inventory = {}

    n = int(input("Enter number of items: "))
    for i in range(n):
        print(f"\nItem {i+1}")
        item = input("Enter item name: ").strip().lower()
        quantity = float(input("Enter quantity: "))
        unit = input("Enter unit (kg/litres/grams etc): ").strip().lower()
        low = float(input(f"Enter LOW threshold for {item} ({unit}): "))
        high = float(input(f"Enter HIGH threshold for {item} ({unit}): "))

        # Update or add item to inventory
        inventory[item] = {
            "quantity": quantity,
            "unit": unit,
            "low": low,
            "high": high
        }

    # Save updated inventory to JSON file
    with open(json_file, "w") as f:
        json.dump({"inventory": inventory}, f, indent=4)

    print("\n📦 Inventory List and Stock Categories:")
    for item_name, data in inventory.items():
        quantity = data["quantity"]
        unit = data["unit"]
        low = data["low"]
        high = data["high"]

        # Dynamic classification
        if quantity <= low:
            category = "Low"
        elif quantity <= high:
            category = "Medium"
        else:
            category = "High"

        print(f"{item_name.title()}: {quantity} {unit} — {category} Stock (Low ≤ {low}, High > {high})")

if __name__ == "__main__":
    track_inventory()
