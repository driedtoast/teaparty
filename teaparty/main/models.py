from django.db import models


class CloudAccount(models.Model):
        account = models.CharField(max_length=100)
        accountKey = models.CharField(max_length=200)
        accountSecretKey = models.CharField(max_length=200)
        type = models.CharField(max_length=100)
        def __unicode__(self):
                return self.account

class Instance(models.Model):
        instanceid = models.CharField(max_length=100)
        type = models.CharField(max_length=100)
        account = models.ForeignKey(CloudAccount)
        def __unicode__(self):
                return self.instanceid


class ServerImage(models.Model):
	imageid = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	created = models.DateTimeField('date created')
	type = models.CharField(max_length=100)
	accountId = models.CharField(max_length=200)
	def __unicode__(self):
        	return self.imageid
	
