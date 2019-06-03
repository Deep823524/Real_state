from django.db import models

class Agent(models.Model):
    agent_id = models.IntegerField()
    agent_Fname = models.CharField(max_length=50)
    agent_Lname = models.CharField(max_length=50)
    agent_email = models.EmailField()
    agent_username = models.CharField(max_length=50)
    agent_password = models.CharField(max_length=10)
    agent_contact = models.BigIntegerField()
    agent_address = models.TextField()
    agent_city = models.CharField(max_length=50)
    agent_state = models.CharField(max_length=50)
    agent_country = models.CharField(max_length=50)
