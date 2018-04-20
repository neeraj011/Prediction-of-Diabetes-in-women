from django.db import models

# Create your models here.
class parameter(models.Model):
	glucose=models.FloatField()
	insulin=models.FloatField()
	blood_pressure=models.FloatField()
	skin_thickness=models.FloatField()
	pregnancies=models.FloatField()
	bmi=models.FloatField()
	age=models.FloatField()
	diabetes_pedigree_function=models.FloatField()

class Document(models.Model):
	document=models.FileField(upload_to='documents/')