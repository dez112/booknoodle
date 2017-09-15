from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=400, blank=True, null=True )
    publishing_line = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=70, blank=True, null=True)
    cover = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Owner(models.Model):
    book_title = models.ForeignKey
    owner = models.CharField(max_length=200)
    rented = models.NullBooleanField(default=False, blank=True)
    rented_by = models.CharField(max_length=200, blank=True, null=True)
    rented_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.owner