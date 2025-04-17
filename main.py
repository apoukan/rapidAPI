#Créer un fichier texte avec vote clé api. plus d'infos sur rapidapi.com
import requests
import pandas

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers":"1","orderBy":"marketCap","orderDirection":"desc","limit":"60","offset":"0"}

with open("api.txt") as file:
	api = file.read().strip()

headers = {
	"x-rapidapi-key": api,
	"x-rapidapi-host": "coinranking1.p.rapidapi.com"
}
#Requète pour se connecter au serveur
response = requests.get(url, headers=headers, params=querystring)

#Créer le Dataframe a partir de la réponse json
data = response.json()
coins = data['data']['coins']
df = pandas.DataFrame(coins)

#Sauvegarder le résultat dans un fichier csv
df.to_csv('crypto_coins.csv')
