# Program to provide gardening advice based on season and plant type

# Function to get user input
def get_user_input():
    """
    Gets user input for season and plant type.

    Returns:
        tuple: (season, plant_type) both as lowercase strings
    """
    # Prompt user for season and plant type
    season = input("Enter the season (summer/winter): ").strip().lower()
    plant_type = input(
        "Enter the type of plant (flower/vegetable): "
    ).strip().lower()
    # Return the inputs as a tuple
    return season, plant_type


# Functions to get gardening advice based on season and plant type
def get_season_advice(season):
    """
    Returns gardening advice based on the season.

    Args:
        season (str): The season (summer, winter, etc.)

    Returns:
        str: Advice for the given season
    """
    # If-else structure to provide advice based on the season
    if season == "summer":
        # Advice for summer season
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        # Advice for winter season
        return "Protect your plants from frost with covers.\n"
    else:
        # Default advice for unrecognized seasons
        return "No advice for this season.\n"


# Function to get plant-specific advice
def get_plant_advice(plant_type):
    """
    Returns gardening advice based on the plant type.

    Args:
        plant_type (str): The type of plant (flower, vegetable, etc.)

    Returns:
        str: Advice for the given plant type
    """
    # If-else structure to provide advice based on the plant type
    if plant_type == "flower":
        # Advice for flower plants
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        # Advice for vegetable plants
        return "Keep an eye out for pests!"
    else:
        # Default advice for unrecognized plant types
        return "No advice for this type of plant."


# Function to generate complete gardening advice
def generate_advice(season, plant_type):
    """
    Generates complete gardening advice by combining season and plant advice.

    Args:
        season (str): The season
        plant_type (str): The type of plant

    Returns:
        str: Complete gardening advice
    """
    # Create an empty string to hold the advice
    advice = ""
    # Get advice for the season and plant type
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    # Return the complete advice
    return advice


# Main function that runs the garden advice program
def main():
    """
    Main function that orchestrates the garden advice program.
    """
    # Get user input
    season, plant_type = get_user_input()

    # Generate advice
    advice = generate_advice(season, plant_type)

    # Print the generated advice
    print("\nGardening Advice:")
    print(advice)


# Run the program only if this script is executed directly
if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
# - Add more seasons (spring, autumn) and plant types.
# - Add input validation for user entries.
