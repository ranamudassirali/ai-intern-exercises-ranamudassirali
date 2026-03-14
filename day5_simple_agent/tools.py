import math


def calculator(expression: str):
    """Evaluates a mathematical expression safely."""
    try:
        # In production, use a safer math parser than eval().
        # Here, eval() is used to demonstrate the tool concept.
        # We ensure the result is returned as a string or number for the agent.
        result = eval(expression, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "pow": pow,
            "sin": math.sin,
            "cos": math.cos
        })
        return result
    except Exception as e:
        return f"Error: {str(e)}"


def get_weather(city: str):
    """Bonus Tool: Mock weather data."""
    # In a real scenario, you'd call an API here.
    weather_data = {
        "tokyo": "20°C, Sunny",
        "london": "12°C, Rainy",
        "new york": "15°C, Cloudy"
    }
    # Clean up the input city string and return data
    target_city = city.lower().strip()
    return weather_data.get(
        target_city,
        f"Weather data not available for {city}."
    )