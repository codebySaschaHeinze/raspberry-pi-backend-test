from django.shortcuts import render


from django.http import JsonResponse

def fruits_list(request):
    fruits = [
  { "name": "Apfel", "weight": 180, "color": "grün", "is_ordered": True},
  { "name": "Banane", "weight": 120, "color": "gelb", "is_ordered": False },
  { "name": "Clementine", "weight": 80, "color": "orange", "is_ordered": True },
  { "name": "Dattel", "weight": 10, "color": "braun", "is_ordered": False },
  { "name": "Erdbeere", "weight": 15, "color": "rot", "is_ordered": False },
  { "name": "Feige", "weight": 50, "color": "lila", "is_ordered": True },
  { "name": "Granatapfel", "weight": 400, "color": "rot", "is_ordered": True },
  { "name": "Himbeere", "weight": 5, "color": "rot", "is_ordered": True },
  { "name": "Indianerbanane", "weight": 150, "color": "grün", "is_ordered": True },
  { "name": "Johannisbeere", "weight": 5, "color": "rot", "is_ordered": False },
  { "name": "Kiwi", "weight": 70, "color": "braun", "is_ordered": False },
  { "name": "Limette", "weight": 60, "color": "grün", "is_ordered": True },
  { "name": "Mango", "weight": 300, "color": "grün", "is_ordered": True },
  { "name": "Nektarine", "weight": 140, "color": "orange", "is_ordered": True },
  { "name": "Orange", "weight": 180, "color": "orange", "is_ordered": False },
  { "name": "Papaya", "weight": 500, "color": "grün", "is_ordered": False },
  { "name": "Quitte", "weight": 250, "color": "gelb", "is_ordered": True },
  { "name": "Rote Beete", "weight": 30, "color": "rot", "is_ordered": False },
  { "name": "Satsuma", "weight": 100, "color": "orange", "is_ordered": True },
  { "name": "Traube", "weight": 5, "color": "lila", "is_ordered": True },
  { "name": "Ugni-Beere", "weight": 2, "color": "rot", "is_ordered": False },
  { "name": "Vanilleschote", "weight": 5, "color": "braun", "is_ordered": False },
  { "name": "Wassermelone", "weight": 5000, "color": "grün", "is_ordered": True },
  { "name": "Ximenia", "weight": 30, "color": "orange", "is_ordered": True },
  { "name": "Yuzu", "weight": 120, "color": "gelb", "is_ordered": True },
  { "name": "Zitrone", "weight": 120, "color": "gelb", "is_ordered": False }
]

    return render(request, "fruits_app/fruitlist.html", {"fruits": fruits})

def info(request):
  return render(request, "fruits_app/info.html")