from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=30, null = False)
    email = models.EmailField(max_length=75)
    contanct = models.CharField(max_length = 10)
    dob = models.DateField()
    city = models.CharField(max_length=30)
    BG = (
        (0, '--NA--'),
        (1, 'A +ve'),
        (2, 'A -ve'),
        (3, 'B +ve'),
        (4, 'B -ve'),
        (5, 'AB +ve'),
        (6, 'AB -ve'),
        (7, 'O +ve'),
        (8, 'O -ve')

    )
    blood_group = models.IntegerField(default = 0, choices = BG)
    MS =(
        (0, 'Married'),
        (1, 'Unmarried'),
    )
    marital_status = models.IntegerField(default=0, choices = MS)
    ACT = (
        (0, 'Active'),
        (1, 'Inactive'),
    )
    active = models.IntegerField(default=0, choices= ACT)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    def __str__(self):
        return self.name

    