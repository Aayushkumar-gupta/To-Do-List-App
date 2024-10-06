from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ToDoList Entity
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)  # Links the item to certain user and on deletion delets all associated entities
    name = models.CharField(max_length=200)     # Stores the name of ToDoList 

    def __str__(self):
        return self.name    #returns the name of todolist
    

# item Entity
class item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)    # Links the item to ToDoList and on deletion delets all associated entities
    text = models.CharField(max_length=200)     # Stores the name of task in todolist 
    complete = models.BooleanField()        # Check box to mark if the task is complete or not

    def __str__(self):
        return self.text        #returns the name of task
    
