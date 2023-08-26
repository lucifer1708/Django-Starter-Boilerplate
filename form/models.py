from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    rollnumber_name = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.rollnumber_name = f"{self.roll_number}_{self.name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}-{self.roll_number}-{self.phone_number}"
