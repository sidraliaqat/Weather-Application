import tkinter as tk
import requests

# Function to get weather details
def get_weather():
    api_key = "3f71ba0ac2d4ac25fd5b940261c988b0"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_entry.get()  # Get the city name from the entry widget
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # Make the request to the weather API
    response = requests.get(complete_url)
    x = response.json()

    # Check if the city is found
    if x["cod"] != "404":
        # Check if 'main' exists in the response before accessing it
        if "main" in x:
            y = x["main"]
            current_temperature = y["temp"] - 273.15  # Convert Kelvin to Celsius
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"].capitalize()

            # Update the label with the weather information
            weather_info.set(
                f"Temperature: {current_temperature:.2f}°C\n"
                f"Pressure: {current_pressure} hPa\n"
                f"Humidity: {current_humidity}%\n"
                f"Description: {weather_description}"
            )
        else:
            weather_info.set("Error: Weather data is unavailable.")
    else:
        weather_info.set("City Not Found")

# Create the main application window
root = tk.Tk()
root.title("Weather Application")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create the entry widget for the user to input the city name
city_label = tk.Label(root, text="Enter city name:", bg="#f0f0f0", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), width=25)
city_entry.pack(pady=5)

# Create a button that triggers the weather request
get_weather_button = tk.Button(
    root, text="Get Weather", command=get_weather, bg="#4CAF50",
    fg="white", font=("Arial", 12)
)
get_weather_button.pack(pady=10)

# Create a label to display the weather information
weather_info = tk.StringVar()
weather_label = tk.Label(
    root, textvariable=weather_info, bg="#f0f0f0", font=("Arial", 12), justify="left"
)
weather_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
