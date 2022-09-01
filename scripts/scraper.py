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


def creating_json(link):
    recipe_js = {}
    recipe_dict = formating_recipe(link)
    recipe_js[f'{link}'] = {}
    recipe_js[f'{link}'].update(recipe_dict)
    filename = 'recipe.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(recipe_js, f, ensure_ascii=False, indent=4)


def update_json(link):
    recipe_dict = formating_recipe(link)
    filename = 'recipe.json'
    with open(filename) as f:
        recipe = json.load(f)
    for i in recipe.keys():
        if i == link:
            print('recipe already in database')
        else:
            recipe[f'{link}'] = {}
            recipe[f'{link}'].update(recipe_dict)

            #with open(filename, 'w', encoding='utf-8') as f:
            #    json.dump(recipe, f, ensure_ascii=False, indent=4)
            
            print(f'new recipe added')


#creating_json('https://www.chefkoch.de/rezepte/1255131230975627/Traenenkuchen-der-beste-Kaesekuchen-der-Welt.html') 
update_json('https://www.chefkoch.de/rezepte/356221121015731/Putenschnitzel-mit-Brokkoli-vom-Blech.html')
     




        