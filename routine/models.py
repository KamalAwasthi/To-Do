from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Todo(models.Model):
	PRIORITY = (
	    (u'Highest', u'Highest'),
	    (u'Average', u'Average'),
	)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="Kamal")
	task = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	priority = models.CharField(blank=True, null=True, max_length=25, choices=PRIORITY, default='None')
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.task