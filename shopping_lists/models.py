from django.db import models

# Create your models here.

class ShoppingLink(models.Model):
    """ Input of the Recipe link """
    recipe_link = models.URLField(max_length=200)
    
    def __str__(self):
        """Return a link representation of the model.""" 
        return self.recipe_link