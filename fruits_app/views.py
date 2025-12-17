from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def fruits_list(request):
    fruits = [
  { "name": "Apfel", "weight": 180, "color": "rot/grün" },
  { "name": "Banane", "weight": 120, "color": "gelb" },
  { "name": "Clementine", "weight": 80, "color": "orange" },
  { "name": "Dattel", "weight": 10, "color": "braun" },
  { "name": "Erdbeere", "weight": 15, "color": "rot" },
  { "name": "Feige", "weight": 50, "color": "lila/grün" },
  { "name": "Granatapfel", "weight": 400, "color": "rot" },
  { "name": "Himbeere", "weight": 5, "color": "rot" },
  { "name": "Indianerbanane", "weight": 150, "color": "grün" },
  { "name": "Johannisbeere", "weight": 5, "color": "rot" },
  { "name": "Kiwi", "weight": 70, "color": "braun/grün" },
  { "name": "Limette", "weight": 60, "color": "grün" },
  { "name": "Mango", "weight": 300, "color": "gelb/orange" },
  { "name": "Nektarine", "weight": 140, "color": "rot/orange" },
  { "name": "Orange", "weight": 180, "color": "orange" },
  { "name": "Papaya", "weight": 500, "color": "orange/grün" },
  { "name": "Quitte", "weight": 250, "color": "gelb" },
  { "name": "Rote Johannisbeere", "weight": 5, "color": "rot" },
  { "name": "Satsuma", "weight": 100, "color": "orange" },
  { "name": "Traube", "weight": 5, "color": "grün/rot" },
  { "name": "Ugni-Beere", "weight": 2, "color": "rot" },
  { "name": "Vanilleschote", "weight": 5, "color": "braun" },
  { "name": "Wassermelone", "weight": 5000, "color": "grün/rot" },
  { "name": "Ximenia", "weight": 30, "color": "orange" },
  { "name": "Yuzu", "weight": 120, "color": "gelb" },
  { "name": "Zitrone", "weight": 120, "color": "gelb" }
]
    return JsonResponse(fruits, safe=False)