from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	author			= models.ForeignKey(User,default=1, on_delete="CASCADE")
	title			= models.CharField(max_length=120, null=True)
	text			= models.TextField(null=True)
	created_date	= models.DateField(auto_now_add=True, null=True)
	published_date  = models.DateField(auto_now_add=False, null=True, blank=True)



	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'id':self.id})


	def __str__(self):
		return self.title


class Comment(models.Model):
    post         	 = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    author       	 = models.CharField(max_length=200)
    text         	 = models.TextField()
    created_date 	 = models.DateField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)


    def __str__(self):
        return self.text