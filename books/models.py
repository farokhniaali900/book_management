from django.db import models

class Book(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
    )
    author = models.CharField(
        max_length=200,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    publication_date = models.DateField()

    def __str__(self):
        return self.title