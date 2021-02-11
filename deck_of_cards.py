import requests

#url = "https://deckofcardsapi.com/api/deck/new/shuffle/?draw_count=6"
url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {'deck_count': "6" }

payload={}
headers = {
  'Cookie': '__cfduid=d19a18e8de6b609b7c3e8a26e3b71b5af1613082131'
}

response = requests.request("GET", url, headers=headers, data=payload, params=querystring)

print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
