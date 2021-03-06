from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Services(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  on_delete = models.CASCADE
  owner = models.ManyToManyField(
      get_user_model(),
  )

  def __str__(self):
    # This must return a string
    return f"'{self.name}'"

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'name': self.name,
        'price': self.price,
    }
