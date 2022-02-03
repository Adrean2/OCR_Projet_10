from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Project(models.Model):
    TYPE_CHOICES = [
        ("B","Back-End"),
        ("F","Front-end"),
        ("I","iOS"),
        ("A","Android"),
    ]
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200,blank=True,null=True)
    type = models.CharField(max_length=1,choices=TYPE_CHOICES)
    contributors = models.ManyToManyField(User,through="Contributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    A = "AUTHOR"
    P = "PARTICIPANT"
    ROLE_CHOICES = [
        (A,"Author"),
        (P,"Participant"),
    ]
    user = models.ForeignKey(User,on_delete=CASCADE,related_name="user")
    project = models.ForeignKey(Project,on_delete=CASCADE)
    role = models.CharField(max_length=11,choices=ROLE_CHOICES,default=P)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=(["user","project"]),name="Unique User/Project"),
            ]

    def __str__(self):
        return f"{self.project.title}  {self.user.username} {self.role}"
    

class Issue(models.Model):
    PRIORITY_CHOICES = [
        ("H","High"),
        ("S","Standard"),
        ("L","Low"),
    ]
    STATUS_CHOICES = [
        ("WIP","Work In Progress"),
        ("F","Finished"),
        ("TD","To Do"),
        ]
    TAG_CHOICES = [
        ("B","Bug"),
        ("I","Improvement"),
        ("T","Task"),
    ]
    description = models.CharField(max_length=200,blank=True,null=True)
    tag = models.CharField(max_length=1,choices=TAG_CHOICES)
    priority = models.CharField(max_length=1,choices=PRIORITY_CHOICES,default="S")
    status = models.CharField(max_length=3,choices=STATUS_CHOICES,default="TD")
    created_time = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(Project,on_delete=CASCADE)
    user = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
        return f" {self.project.title}: {self.description} - {self.user.username}"


class Comment(models.Model):
    description = models.CharField(max_length=400,blank=True,null=True)
    issue = models.ForeignKey(Issue,on_delete=CASCADE)
    user = models.ForeignKey(to=User,on_delete=CASCADE)

    def __str__(self):
        return f" {self.issue.description[0:15]}... -{self.user.username}: {self.description} "