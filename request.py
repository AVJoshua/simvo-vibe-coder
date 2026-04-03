import requests
import json
# GBIF species search API endpoint with parameters
url = "https://api.gbif.org/v1/species/search"

params = {
    "datasetKey": "d7dddbf4-2cf0-4f39-9b2a-bb099caae36c",
    "q": "kangaroo"
}

headers = {
    "accept": "application/json"
}

print("Fetching kangaroo species data from GBIF...")

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    results = data.get('results', [])
    # Print formatted JSON response
    
    extracted = []
    for item in results:
        extracted_item = {
            'scientificName': item.get('scientificName', ''),
            'authorship': item.get('authorship', ''),
            'kingdom': item.get('kingdom', ''),
            'habitats': item.get('habitats', ''),
            'threatStatuses': item.get('threatStatuses', '')
        }
        extracted.append(extracted_item)
    print(json.dumps(extracted, indent=2))
    
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)