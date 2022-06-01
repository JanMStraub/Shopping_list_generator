from recipe_scrapers import scrape_me
scraper = scrape_me('https://www.chefkoch.de/rezepte/100961040660758/Curry-Gemuese-mit-Tofu.html')


print(scraper.ingredients())