import requests

url = "https://amazon-products1.p.rapidapi.com/product"

querystring = {"country":"US","asin":"0975277324"}

headers = {
    'x-rapidapi-host': "amazon-products1.p.rapidapi.com",
    'x-rapidapi-key': "a37dc52e13msh35033016ac120cdp14ec8ejsnf3065d883aca"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)