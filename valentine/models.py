from django.db import models


class Valentine(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    message = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name}, Date: {self.date}, Message: {self.message}"
