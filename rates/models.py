from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=50)

    def __str__(self):
        return self.code

