from django.http import JsonResponse
import requests
import json
import os

def home_view(request, id):
    api_url = f"http://pokeapi.co/api/v2/pokemon/{id}/"
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]
    pokeid = body["id"]
    types = body["types"]
    key = os.environ.get("GIPHY_KEY")
    url = (f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={name}&rating=g")
    gifres = requests.get(url)
    gifbody = json.loads(gifres.content)
    gifurl = gifbody["data"][0]["url"]

    return JsonResponse({ "message": "ok", "name": name, "id": pokeid, "types": types, "gif": gifurl})