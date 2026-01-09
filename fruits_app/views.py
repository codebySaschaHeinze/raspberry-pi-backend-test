from django.shortcuts import render


from django.http import JsonResponse

def fruits_list(request):
    fruits = [
  { "name": "Apfel", "weight": 180, "color": "rot", "is_ordered": True, "img": "fruits_app/img/apfel.png" },
  { "name": "Banane", "weight": 120, "color": "gelb", "is_ordered": False, "img": "fruits_app/img/banane.png" },
  { "name": "Clementine", "weight": 80, "color": "orange", "is_ordered": True, "img": "fruits_app/img/clementine.png" },
  { "name": "Dattel", "weight": 10, "color": "braun", "is_ordered": False, "img": "fruits_app/img/dattel.png" },
  { "name": "Erdbeere", "weight": 15, "color": "rot", "is_ordered": False, "img": "fruits_app/img/erdbeere.png" },
  { "name": "Feige", "weight": 50, "color": "lila", "is_ordered": True, "img": "fruits_app/img/feige.png" },
  { "name": "Granatapfel", "weight": 400, "color": "rot", "is_ordered": True, "img": "fruits_app/img/granatapfel.png" },
  { "name": "Himbeere", "weight": 5, "color": "rot", "is_ordered": True, "img": "fruits_app/img/himbeere.png" },
  { "name": "Indianerbanane", "weight": 150, "color": "grün", "is_ordered": True, "img": "fruits_app/img/indianerbanane.png" },
  { "name": "Johannisbeere", "weight": 5, "color": "rot", "is_ordered": False, "img": "fruits_app/img/johannisbeere.png" },
  { "name": "Kiwi", "weight": 70, "color": "braun", "is_ordered": False, "img": "fruits_app/img/kiwi.png" },
  { "name": "Limette", "weight": 60, "color": "grün", "is_ordered": True, "img": "fruits_app/img/limette.png" },
  { "name": "Mango", "weight": 300, "color": "grün", "is_ordered": True, "img": "fruits_app/img/mango.png" },
  { "name": "Nektarine", "weight": 140, "color": "orange", "is_ordered": True, "img": "fruits_app/img/nektarine.png" },
  { "name": "Orange", "weight": 180, "color": "orange", "is_ordered": False, "img": "fruits_app/img/orange.png" },
  { "name": "Papaya", "weight": 500, "color": "grün", "is_ordered": False, "img": "fruits_app/img/papaya.png" },
  { "name": "Quitte", "weight": 250, "color": "gelb", "is_ordered": True, "img": "fruits_app/img/quitte.png" },
  { "name": "Rote Beete", "weight": 30, "color": "rot", "is_ordered": False, "img": "fruits_app/img/rotebeete.png" },
  { "name": "Satsuma", "weight": 100, "color": "orange", "is_ordered": True, "img": "fruits_app/img/satsuma.png" },
  { "name": "Traube", "weight": 5, "color": "lila", "is_ordered": True, "img": "fruits_app/img/traube.png" },
  { "name": "Ugni-Beere", "weight": 2, "color": "rot", "is_ordered": False, "img": "fruits_app/img/ugnibeere.png" },
  { "name": "Vanilleschote", "weight": 5, "color": "braun", "is_ordered": False, "img": "fruits_app/img/vanille.png" },
  { "name": "Wassermelone", "weight": 5000, "color": "grün", "is_ordered": True, "img": "fruits_app/img/wassermelone.png" },
  { "name": "Ximenia", "weight": 30, "color": "gelb", "is_ordered": True, "img": "fruits_app/img/ximenia.png" },
  { "name": "Yuzu", "weight": 120, "color": "gelb", "is_ordered": True, "img": "fruits_app/img/yuzu.png" },
  { "name": "Zitrone", "weight": 120, "color": "gelb", "is_ordered": False, "img": "fruits_app/img/zitrone.png" }
]

    return render(request, "fruits_app/fruitlist.html", {"fruits": fruits})

def info(request):
  return render(request, "fruits_app/info.html")