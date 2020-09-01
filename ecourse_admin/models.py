from django.db import models
import uuid;
# Create your models here.
class adminlogin(models.Model):
    name = models.CharField(max_length=200);
    email = models.CharField(max_length=200);
    password = models.CharField(max_length=200);

class websitedetails(models.Model):
    websitename = models.CharField(max_length=200);
    aboutwebsite = models.TextField();


class addcourse(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, ); 
    title = models.CharField(max_length=200);
    shortdescription=models.TextField(default="")
    description= models.TextField(default="");
    status = models.CharField(max_length=200,default="");
    image = models.TextField()
    # image = models.ImageField(upload_to="images/",default="")



class courses(models.Model):
    course_id = models.TextField()
    videos = models.TextField()
    # videos = models.FileField(upload_to="videos/", blank=True)


class userlogin(models.Model):
    studentid = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False);
    name = models.CharField(max_length=200);
    email = models.CharField(max_length=200);
    password = models.CharField(max_length=200);


class myvid(models.Model):
    studentid = models.TextField();
    course_id = models.TextField();
        
   
class userprofilepic(models.Model):
    studentid = models.TextField();
    profile_pic=models.TextField();         
                
