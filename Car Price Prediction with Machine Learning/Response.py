import requests

url = "http://127.0.0.1:5000/predict"  # Ensure Flask is running at this URL
data = {
    "Fuel_Type": "Petrol",
    "Selling_type": "Dealer",
    "Transmission": "Manual",
    "Present_Price": 5.59,
    "Driven_kms": 27000,
    "Owner": 0, 
    "Car_Age": 5
}

# Send POST request
response = requests.post(url, json=data)

# Print the response from the API
print(response.json())
