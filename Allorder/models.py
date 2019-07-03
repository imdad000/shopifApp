from django.db import models

class Product(models.Model):
    title           = models.CharField(max_length=120)
    id1             = models.TextField()
    def __str__(self):
        return self.title


class Customer(models.Model):
	name = models.CharField(max_length=80, null=True)
	email = models.CharField(max_length=20, null=True)
	customer_id = models.CharField(max_length=250,unique=True)
	contactno = models.IntegerField(null=True)
	# class Meta:
 #        unique_together = ["name","email","customer_id","contactno"]

	def __str__(self):
		return self.name