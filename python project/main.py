import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = "ef1e77a1db1b531013d96bbc13d482d9"  # Use your actual API key here
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            result_label.config(text=f"Weather in {city_name}: {temp}°C, {description}")
        else:
            result_label.config(text="City not found or API error!")
    except Exception as e:
        result_label.config(text="Error connecting to API.")
        print("Error:", e)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create UI elements
tk.Label(root, text="Enter city name:", font=("Arial", 14)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
