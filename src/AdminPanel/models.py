from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class Article(models.Model):
	Title = models.CharField(max_length=50)
	Organization = models.CharField(max_length=50, blank=True)
	Location = models.CharField(max_length=100)
	Description = models.TextField(blank=True)
	Start = models.DateTimeField(default=datetime.now, blank=True)
	End = models.DateTimeField(default=datetime.now, blank=True)
	Link = models.CharField(max_length = 500, blank=True)
	Tag = models.CharField(max_length = 20)
	Flyer = models.FileField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.Title + ' - ' + self.Organization

	def get_absolute_url(self):
		return reverse('adminpanel:event-details', kwargs={'pk': self.pk})
				