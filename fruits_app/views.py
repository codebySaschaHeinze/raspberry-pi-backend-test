from django.shortcuts import render


from django.http import JsonResponse

def fruits_list(request):
    fruits = [
  { "name": "Apfel", "weight": 180, "color": "rot", "is_ordered": True, "img": },
  { "name": "Banane", "weight": 120, "color": "gelb", "is_ordered": False, "img":  },
  { "name": "Clementine", "weight": 80, "color": "orange", "is_ordered": True, "img":  },
  { "name": "Dattel", "weight": 10, "color": "braun", "is_ordered": False, "img":  },
  { "name": "Erdbeere", "weight": 15, "color": "rot", "is_ordered": False, "img":  },
  { "name": "Feige", "weight": 50, "color": "lila", "is_ordered": True, "img":  },
  { "name": "Granatapfel", "weight": 400, "color": "rot", "is_ordered": True, "img":  },
  { "name": "Himbeere", "weight": 5, "color": "rot", "is_ordered": True, "img":  },
  { "name": "Indianerbanane", "weight": 150, "color": "grün", "is_ordered": True, "img":  },
  { "name": "Johannisbeere", "weight": 5, "color": "rot", "is_ordered": False, "img":  },
  { "name": "Kiwi", "weight": 70, "color": "braun", "is_ordered": False, "img":  },
  { "name": "Limette", "weight": 60, "color": "grün", "is_ordered": True, "img":  },
  { "name": "Mango", "weight": 300, "color": "grün", "is_ordered": True, "img":  },
  { "name": "Nektarine", "weight": 140, "color": "orange", "is_ordered": True, "img":  },
  { "name": "Orange", "weight": 180, "color": "orange", "is_ordered": False, "img":  },
  { "name": "Papaya", "weight": 500, "color": "grün", "is_ordered": False, "img":  },
  { "name": "Quitte", "weight": 250, "color": "gelb", "is_ordered": True, "img":  },
  { "name": "Rote Beete", "weight": 30, "color": "rot", "is_ordered": False, "img":  },
  { "name": "Satsuma", "weight": 100, "color": "orange", "is_ordered": True, "img":  },
  { "name": "Traube", "weight": 5, "color": "lila", "is_ordered": True, "img":  },
  { "name": "Ugni-Beere", "weight": 2, "color": "rot", "is_ordered": False, "img":  },
  { "name": "Vanilleschote", "weight": 5, "color": "braun", "is_ordered": False, "img":  },
  { "name": "Wassermelone", "weight": 5000, "color": "grün", "is_ordered": True, "img":  },
  { "name": "Ximenia", "weight": 30, "color": "orange", "is_ordered": True, "img":  },
  { "name": "Yuzu", "weight": 120, "color": "gelb", "is_ordered": True, "img":  },
  { "name": "Zitrone", "weight": 120, "color": "gelb", "is_ordered": False, "img":  }
]

    return render(request, "fruits_app/fruitlist.html", {"fruits": fruits})

def info(request):
  return render(request, "fruits_app/info.html")