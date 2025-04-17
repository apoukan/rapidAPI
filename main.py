import requests

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
	"x-rapidapi-key": "e82fc1d035mshc5c8a8cbe9c3efbp15598cjsndfdf86bf2bd2",
	"x-rapidapi-host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
