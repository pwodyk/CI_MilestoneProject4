from django.db import models
from django.contrib.auth.models import User
import datetime

TICKET_TYPES = (
    ('F', 'Feature'),
    ('B', 'Bug'),
)
    
TICKET_STATUS = (
    ("0", "Highest-paid"),
    ("1", "Completed"),
    ("2", "In Progress"),
    ("3", "Submitted"),
    ("4", "On Hold"),
    ("5", "Abandoned"),
    
    
)

class Ticket(models.Model):
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    contibutions = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    ticket_type = models.CharField(max_length=1, choices=TICKET_TYPES)
    status = models.CharField(max_length=1, default="3", choices=TICKET_STATUS)
    progress = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="author")
    upvoted_by = models.ManyToManyField(User, related_name="users")
    
    
    def __str__(self):
        return "{0}{1} : {2} @ {3}".format(self.ticket_type, str(self.id), self.name, self.contibutions if self.ticket_type == "F" else self.upvoted_by.count() ) 