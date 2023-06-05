from recipe_scrapers import scrape_me
import pandas as pd
from IPython import embed

"""
TODOs
    * schreiben Update Funktion für DF
    * migrieren DF in SQL
    * Unittests
    * Kommentare für Funktionen
    * Beschreibung
"""

def get_recipe(link):
    """
    Retrieves the ingredients and recipe name from a given recipe link.

    Args:
        link (str): The URL of the recipe page to scrape.

    Returns:
        tuple: A tuple containing two elements - the list of ingredients and the recipe name.

    Raises:
        Any exceptions raised during the scraping process.

    """

    # Initialize a web scraper for the provided link
    scraper = scrape_me(link)

    # Extract the list of ingredients from the scraper
    ingredients = scraper.ingredients()

    # Extract the recipe name from the scraper
    recipe_name = scraper.title()

    # Return the ingredients and recipe name as a tuple
    return ingredients, recipe_name




def formating_recipe(link):
    ingredients, recipe_name = get_recipe(link) 
    ingredients = [item.split(',', 1)[0].strip() for item in ingredients]
    
    menge = []
    einheit = []
    ingredient = []

    for item in ingredients:
        # split the string into a list of words
        words = item.split()
        if len(words) == 3: 
            menge.append(words[0])
            einheit.append(words[1])
            ingredient.append(words[2])  

        elif len(words) == 2: 
            menge.append(words[0])
            einheit.append('')
            ingredient.append(words[1])

        elif len(words) == 1:
            menge.append('')
            einheit.append('')
            ingredient.append(words[0])
        else:
            raise ValueError('There are no ingredients!')
    # create an index for the recipe for the identification in th
    # e database
    index = 0
    
    df_index = pd.DataFrame({"Name": recipe_name, "ID": [index]})

    df = pd.DataFrame({"Zutat": ingredient, 
                    "Menge": menge, 
                    "Einheit": einheit, 
                    "ID": len(ingredient)*[index]})

if __name__ == '__main__':
    print("Programm started") 
    formating_recipe('https://www.chefkoch.de/rezepte/1255131230975627/Traenenkuchen-der-beste-Kaesekuchen-der-Welt.html')
    
    # creating_json('https://www.chefkoch.de/rezepte/1255131230975627/Traenenkuchen-der-beste-Kaesekuchen-der-Welt.html') 
    # update_json('https://www.chefkoch.de/rezepte/1137791220019690/Illes-leichter-und-leckerer-Thunfisch-Tomaten-Salat.html')