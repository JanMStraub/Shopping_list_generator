from recipe_scrapers import scrape_me
import json


scraper = scrape_me('https://www.chefkoch.de/rezepte/100961040660758/Curry-Gemuese-mit-Tofu.html')
ingr_data = scraper.ingredients()
recipe_name = scraper.title()
ingr_data = [i.split(',', 1)[0].strip() for i in ingr_data]

recipe_dict = {'name':[], 'ingredients':[]}
recipe_dict['name'].append(recipe_name)
recipe_dict['ingredients'].append(ingr_data)


with open('ingr_data.json', 'w', encoding='utf-8') as f:
        json.dump(recipe_dict, f, ensure_ascii=False, indent=4)

