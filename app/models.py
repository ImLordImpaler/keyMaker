from django.db import models

# Create your models here.

class Node(models.Model):
	name = models.CharField(max_length=100 , null=True , blank=True)
	desc = models.TextField()
	price = models.IntegerField(default=0)
	