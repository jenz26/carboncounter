# co2_calc.py
# Module to calculate CO₂ emissions based on user inputs and predefined estimates

import json
from pathlib import Path


def load_estimates():
    """
    Load CO₂ emission estimates from the JSON file.
    Returns:
        dict: A dictionary containing emission estimates per activity.
    """
    data_path = Path(__file__).resolve().parent.parent / "data" / "co2_estimates.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


def calculate_emissions(user_input, estimates):
    """
    Calculate the total CO₂ emissions based on user inputs.
    
    Args:
        user_input (dict): Dictionary containing quantities of digital activities.
        estimates (dict): Dictionary of CO₂ emissions per activity.

    Returns:
        float: Total CO₂ emissions in grams.
    """
    total = 0
    for key, value in user_input.items():
        co2 = estimates.get(key, {}).get("co2_g", 0)
        total += value * co2
    return total


def emissions_by_activity(user_input, estimates):
    """
    Calculate CO₂ emissions per activity in descending order.
    
    Args:
        user_input (dict): Dictionary containing quantities of digital activities.
        estimates (dict): Dictionary of CO₂ emissions per activity.

    Returns:
        dict: Dictionary of labeled activities and their total emissions.
    """
    activity_emissions = {}
    for key, quantity in user_input.items():
        co2 = estimates.get(key, {}).get("co2_g", 0)
        total = quantity * co2
        if quantity > 0:
            label = estimates.get(key, {}).get("label", key)
            activity_emissions[label] = total
    return dict(sorted(activity_emissions.items(), key=lambda item: item[1], reverse=True))