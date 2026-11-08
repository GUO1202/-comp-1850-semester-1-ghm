# Week 1.3, Session 2: Home Sensor Filtering

home_sensors = {"Living Room Thermostat": 85, "Front Door Lock": 15, "Kitchen Smoke Detector": 90, "Basement Flood Sensor": 8}
low_battery = {name: battery for name, battery in home_sensors.items() if battery < 20}
print(low_battery)
