import pprint
pp = pprint.PrettyPrinter()


def create_listed_file():
  listed_file = []
  with open('recipes.txt','r') as recipes:
    for line in recipes:
      if line.strip():
        listed_file.append(line.strip())
  if len(listed_file): 
    return listed_file
  else:
    return print('Can not create CookBook from an empty list!')

def create_cook_book():

  listed_file = create_listed_file()
  cook_book = {}

  n = 0
  while n < len(listed_file):

    dish_name = listed_file[n]
    ingredients_list = []
    m = 0    
    while m < int(listed_file[n + 1]):
      ingredient = listed_file[n + 2 + m].split('|')
      ingredients_list.append({'ingredient_name': ingredient[0].strip(), 'quantity': int(ingredient[1]), 'measure': ingredient[2].strip()})
      m += 1

    cook_book.update({dish_name:ingredients_list})
    n += (2 + m)

  return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  cook_book = create_cook_book()
  shop_list = {}
  for dish in dishes: 
    for recepie in cook_book.keys():
      if recepie == dish:
        for ingredient in cook_book[recepie]:
          if ingredient['ingredient_name'] not in shop_list.keys():
            shop_list.update({ingredient['ingredient_name']: {'measure' : ingredient['measure'], 'quantity' : ingredient['quantity'] * person_count}})
          else:
            shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
  return(shop_list)

pp.pprint(create_cook_book())
pp.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))


