
# Create your models here.
from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)

    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        # Redirects to the detail view of the newly created recipe
        return reverse('recipe_detail', kwargs={'pk': self.pk})  