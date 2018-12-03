from django.db import models

# Create your models here.

# Create your models here.
class Cluster(models.Model):
	cluster_text = models.CharField(max_length=200)

class Station(models.Model):
    def __str__(self):
    	return str(self.cluster_id)
    question_text = models.CharField(max_length=200)
    cluster_id = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
	#def __str__(self):
	#	return self.choice_text
	question = models.ForeignKey(Station, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Strategy(models.Model):
	def __str__(self):
		return self.strategy_text
	strategy_text = models.CharField(max_length=200)