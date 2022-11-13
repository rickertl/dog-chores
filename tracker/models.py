from django.db import models
from django.contrib.auth.models import User  # Required to assign User care_giver


# Chore Event
class ChoreEvent(models.Model):
    """Model representing a chore event."""

    CHORE_TYPES = (
        ('f', 'Feed'),
        ('w', 'Walk'),
        ('p1', 'Pee'),
        ('p2', 'Poop'),
    )

    type = models.CharField(max_length=2, choices=CHORE_TYPES)

    dog = models.ForeignKey('Dog', on_delete=models.SET_NULL, null=True)

    care_giver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.type


# Family
class Family(models.Model):
    """Model representing a family."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


# Dog 
class Dog(models.Model):
    """Model representing a dog."""
    name = models.CharField(max_length=200)

    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        """String for representing the Model object."""
        return self.name
