from django.db import models

class Order(models.Model):
	STATUS = (
			('Delivered', 'Delivered'),
			)
