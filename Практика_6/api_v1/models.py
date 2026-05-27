from django.db import models


class Appointment(models.Model):
    pet = models.ForeignKey('Pet', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING)
    appointment_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Owner(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pet'
