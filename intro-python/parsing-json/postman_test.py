import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {
  'Cookie': '__cfduid=df4af11bb15b9e686849b3d382f1d758d1585856722'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)