from django.db import models

class Instance(models.Model):
	id = models.CharField(max_length=100)
        type = models.CharField(max_length=100)
	def __unicode__(self):
        	return self.id

class ServerImage(models.Model):
	id = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	created = models.DateTimeField('date created')
	type = models.CharField(max_length=100)
	accountId = models.CharField(max_length=200)
	def __unicode__(self):
        	return self.id
	
