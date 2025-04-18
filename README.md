# Récupération des données de cryptomonnaies avec l'API CoinRanking

Ce script Python permet de récupérer les 60 principales cryptomonnaies classées par capitalisation boursière via l'API [CoinRanking](https://rapidapi.com/Coinranking/api/coinranking1) disponible sur RapidAPI, et d’enregistrer les données dans un fichier CSV.

## Prérequis
- Python 3.7 ou plus
- Une clé API RapidAPI pour CoinRanking
- Créez un fichier nommé api.txt dans le même dossier que le script Python, et collez-y uniquement votre clé API.

##  Installation
```bash
git clone https://github.com/apoukan/rapidAPI.git
cd rapidAPI
pip install -r requirements.txt
python main.py
#or
chmod a+x main.py && ./main.py
