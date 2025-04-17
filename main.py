#Créer un fichier texte avec vote clé api. plus d'infos sur rapidapi.com
import requests

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers":"1","orderBy":"marketCap","orderDirection":"desc","limit":"60","offset":"0"}

with open("api.txt") as file:
	api = file.read().strip()

headers = {
	"x-rapidapi-key": api,
	"x-rapidapi-host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
