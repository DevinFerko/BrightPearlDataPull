import requests
import json

# Replace with your Brightpearl API details
BRIGHTPEARL_API_URL = 'https://ws-eu1.brightpearl.com/public-api/{account_id}/'
API_KEY = 'YOUR_API_KEY'
ACCOUNT_ID = 'YOUR_ACCOUNT_ID'

# Function to get the sales data
def get_sales_data():
    headers = {
        'brightpearl-auth': API_KEY,
        'Content-Type': 'application/json'
    }

    endpoint = f'{BRIGHTPEARL_API_URL}/order-service/order-search'

    # Example payload for searching orders
    payload = {
        "firstResult": 0,
        "maxResults": 100,
        "orderTypeCodes": ["SO"],  # Sales orders
        "orderStatusIds": [4, 5, 6]  # Example status IDs
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        print(response.text)
        return None

# Main function
if __name__ == '__main__':
    sales_data = get_sales_data()
    if sales_data:
        # Print or process the sales data
        print(json.dumps(sales_data, indent=4))