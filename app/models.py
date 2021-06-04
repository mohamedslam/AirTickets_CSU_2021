"""
Definition of models.
"""

from django.db import models
# Create your models here.

# model UserData
class Users(models.Model):
    UserId=models.IntegerField()
    UserName=models.CharField(max_length=20)
    EnFullName=models.CharField(max_length=100)
    Gender=models.BooleanField(default=True)
    DateOfBirth=models.CharField(max_length=100)
    PassportNumber=models.CharField(max_length=10)
    Nationalty=models.CharField(max_length=20)    
    Password=models.CharField(max_length=20)
    Email=models.CharField(max_length=100)
    Notice=models.CharField(max_length=300)
    IsActive=models.BooleanField(default=True)

# model Twons and AirPort
class AirPorts(models.Model):
    AirPortsId=models.CharField(max_length=10)
    PortName=models.CharField(max_length=30)
    PortShortName=models.CharField(max_length=30)
    Country=models.CharField(max_length=10)
    ParantId=models.CharField(max_length=10)
    IsActive=models.BooleanField()

    # model UseSearch Results
class UserSearch(models.Model):
    UserId=models.IntegerField()
    From_Town=models.CharField(max_length=20)
    To_Town=models.CharField(max_length=20)
    OneWay=models.BooleanField()
    adultCount=models.IntegerField()
    ChildCount=models.IntegerField()
    IsSent=models.BooleanField(default=True)

class flightsData(models.Model):
    flightId=models.CharField(max_length=20)
    FromAirPort=models.CharField(max_length=30)
    ToAirport=models.CharField(max_length=30)
    TakeOffTime=models.DateTimeField()
    ArrivalTime=models.DateTimeField()
    FlightStopAirPorts=models.CharField(max_length=10)
    TicketCost=models.IntegerField()
    TaxCost=models.IntegerField()
    InDate=models.DateTimeField()


class BookingData(models.Model):
    BokingId=models.CharField(max_length=20)
    BUserId=models.IntegerField()
    BflightId=models.CharField(max_length=20)
    BookingDate=models.DateTimeField()
    IsSent=models.BooleanField(default=True)
    IsConfirmed=models.BooleanField()
    IsPaid=models.BooleanField(default=True)
    