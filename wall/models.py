from django.db import models
from loginapp.models import User
import re
import bcrypt

class Message(models.Model):
    user_id = models.ForeignKey(User, related_name = 'postbyuser', on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name = 'commentonmessage', on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, related_name = 'commentbyuser', on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)