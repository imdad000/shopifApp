from django.db import models

class Product(models.Model):
    title           = models.CharField(max_length=120)
    id1             = models.TextField()
    def __str__(self):
        return self.title


class Customer(models.Model):
	name = models.CharField(max_length=80)
	email = models.CharField(max_length=20)
	customer_id = models.CharField(max_length=250)
	contactno = models.IntegerField()

	def __str__(self):
		return self.name