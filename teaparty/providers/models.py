from django.db import models

class ProviderType(models.Model):
        type = models.CharField(max_length=100)
        providerClass = models.CharField(max_length=200)
	def __unicode__(self):
        	return self.type

class Provider(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField('date created')
	type = models.ForeignKey(ProviderType)
	accountId = models.CharField(max_length=200)
	accountKey = models.CharField(max_length=200)
	secretKey = models.CharField(max_length=200)
	def __unicode__(self):
        	return self.name
	
