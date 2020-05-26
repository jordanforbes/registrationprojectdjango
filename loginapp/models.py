from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def reg_validator(self, post_data):
        print('validator time')
        print('post data:',post_data)
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(post_data['firstName'])<2:
            errors['firstName'] = 'first name must be more than 2 characters'
        if len(post_data['lastName'])<2:
            errors['lastName'] = 'last name must be more than 2 characters'
        if len(post_data['email'])==0:
            errors['emailrequired'] = 'email cannot be empty'
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['emailwrong'] = 'Invalid Email'
        if len(post_data['pw'])<8:
            errors['pw'] = 'password must be at least 8 characters'
        if post_data['pw'] != post_data['confpw']:
            errors['confpw'] = "password must match confirmation"
        return errors
    
    def loginValidator(self, postData):
        print('loginValidator, below is the post data')
        print(postData)
        errors = {}
        if len(postData['email']) == 0:
            errors['emailrequired'] = "Email is required"
        else:
            usersWithEmail = User.objects.filter(email = postData['email'])
            print(usersWithEmail)
            if len(usersWithEmail)==0:
                errors['emailnotregistered'] = 'email not found'
            else: 
                usertocheck = usersWithEmail[0]
                if bcrypt.checkpw(postData['pw'].encode(), usertocheck.password.encode()):
                    print('password matches')
                else:
                    errors['pwwrong'] = 'password is incorrect'
        return errors
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255 )
    last_name = models.CharField(max_length= 255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    objects = UserManager()
    
class Item(models.Model):
    name = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = "items_uploaded", on_delete = models.CASCADE)
    favorites = models.ManyToManyField(User, related_name = 'items_favorited')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)