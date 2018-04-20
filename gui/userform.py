from django import forms
from .models import parameter,Document


class DataForm(forms.ModelForm):
	glucose=forms.FloatField(label='Glucose')
	insulin=forms.FloatField(label='Insulin')
	blood_pressure=forms.FloatField(label='Blood Pressure')
	skin_thickness=forms.FloatField(label='Skin Thickness')
	pregnancies=forms.FloatField(label='Pregnancies')
	bmi=forms.FloatField(label='BMI')
	age=forms.FloatField(label='Age')
	diabetes_pedigree_function=forms.FloatField(label='Diabetes Pedigree Function')

	class Meta:
		model = parameter
		fields = ('glucose','insulin','blood_pressure','skin_thickness','pregnancies','bmi','age','diabetes_pedigree_function')

class DocumentForm(forms.ModelForm):
	document=forms.FileField(label ='Choose file: ')
	class Meta:
		model=Document
		fields=('document',)