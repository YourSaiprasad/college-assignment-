import tkinter as tk
from tkinter import messagebox
from main import get_weather_data  # Import the function from main.py

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name")
        return

    result = get_weather_data(city_name)
    if "error" in result:
        result_label.config(text=result["error"])
    else:
        result_label.config(text=f"Weather in {city_name}: {result['temp']}°C, {result['description']}")

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
