from recipe_scrapers import scrape_me
import json
from IPython import embed

def get_recipe(link):
    scraper = scrape_me(link)
    ingr_data = scraper.ingredients()
    recipe_name = scraper.title()
    
    return ingr_data, recipe_name


def formating_recipe(link):
    ingr_data, recipe_name = get_recipe(link) 
    ingr_data = [i.split(',', 1)[0].strip() for i in ingr_data]
    recipe_dict = {'name':[], 'ingredients':[]}
    recipe_dict['name'].append(recipe_name)
    recipe_dict['ingredients'].extend(ingr_data)
    
    return recipe_dict


def recipe_to_json(link):
    recipe_dict = formating_recipe(link)
    filename = 'recipe.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(recipe_dict, f, ensure_ascii=False, indent=4)


def update_json(link):
    recipe_dict = formating_recipe(link)
    filename = 'recipe.json'

    with open(filename) as f:
        recipe = json.load(f)

    embed()
    exit()
    recipe.update(recipe_dict)
  

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(recipe, f, ensure_ascii=False, indent=4)


def testing_if_recipe_in_json(new_link):
    filename = 'recipe.json'
    _, recipe_name_new = get_recipe(new_link)
    with open(filename) as f:
        recipe= json.load(f)
    for name in recipe['name']:
        if name == recipe_name_new:
            print(f"{name} is already in database")
        else:
            update_json(new_link)
            print("hey")
    
testing_if_recipe_in_json('https://www.chefkoch.de/rezepte/1255131230975627/Traenenkuchen-der-beste-Kaesekuchen-der-Welt.html')
         
                




        