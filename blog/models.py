from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
""" class ShoppingListItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField
    #id = models.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name """
    
""" class ShoppingListQuantity(models.Model):
    shoppingListItem = ShoppingListItem
    #id
    #quantity = 
    def __str__(self):
        return self.id """

""" class ShoppingList(models.Model):
    #id
    name  = models.CharField(max_length=255)
    created_date = models.DateTimeField(
            default=timezone.now)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    items = []
    def __str__(self):
        return self.name """
    


