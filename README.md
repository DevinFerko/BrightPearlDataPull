# Brightpearl API Sales Data Fetcher

This script retrieves sales data from the Brightpearl API. It searches for sales orders based on predefined criteria and prints the resulting data in a readable JSON format.

## Prerequisites

- Python 3.x
- `requests` library

## Setup

1. Install the `requests` library if you haven't already:

   ```sh
   pip install requests
   ```

2. Replace the placeholder values in the script with your actual Brightpearl API details:

   ```python
   BRIGHTPEARL_API_URL = 'https://ws-eu1.brightpearl.com/public-api/{account_id}/'
   API_KEY = 'YOUR_API_KEY'
   ACCOUNT_ID = 'YOUR_ACCOUNT_ID'
   ```

## Usage

1. Ensure your Brightpearl API credentials and account ID are correctly set in the script.
2. Run the script:

   ```sh
   python script_name.py
   ```

3. The script will fetch the sales data and print it in a formatted JSON structure.

## Script Details

- **Endpoint**: The script targets the `order-service/order-search` endpoint of the Brightpearl API to retrieve sales orders.
- **Headers**: It uses the Brightpearl API key for authentication and specifies the content type as JSON.
- **Payload**: The payload in the script is set to search for sales orders (`orderTypeCodes: ["SO"]`) with specific status IDs (`orderStatusIds: [4, 5, 6]`).

### Example Payload

```json
{
    "firstResult": 0,
    "maxResults": 100,
    "orderTypeCodes": ["SO"],
    "orderStatusIds": [4, 5, 6]
}
```

## Response Handling

- If the API call is successful (`status_code == 200`), the script prints the sales data in a formatted JSON structure.
- If the API call fails, it prints the error status code and message.

## Notes

- Adjust the `orderTypeCodes` and `orderStatusIds` in the payload as needed to match your search criteria.
- The script currently fetches up to 100 sales orders starting from the first result. Modify the `firstResult` and `maxResults` values in the payload to change the range of results fetched.

## Example Output

```json
{
    "response": {
        "results": [
            {
                "id": 12345,
                "orderTypeCode": "SO",
                "orderStatusId": 5,
                ...
            },
            ...
        ]
    }
}
```

## Troubleshooting

- Ensure your API key and account ID are correct.
- Verify that your network connection allows access to the Brightpearl API.
- Check Brightpearl API documentation for any updates or changes to the API endpoints and parameters.