# importing required modules
import os
import csv
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.views import login
from django.conf import settings
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import io
import csv
import ast
from .userform import DataForm,DocumentForm
from .p2 import mlp,mlp_csv
from django.views.generic import View
from .models import parameter
from django.template.loader import get_template
from .graph import graph
f1=io.BytesIO()

class UserHome(TemplateView):
	template_name = 'input.html'

	def get(self, request):
		form1=DataForm()
		return render(request, self.template_name, {'form1' : form1})

	def post(self, request):
		form1 = DataForm(request.POST)
		if form1.is_valid():
			form1.save()
			glucose=form1.cleaned_data['glucose']
			insulin=form1.cleaned_data['insulin']
			blood_pressure=form1.cleaned_data['blood_pressure']
			skin_thickness=form1.cleaned_data['skin_thickness']
			pregnancies=form1.cleaned_data['pregnancies']
			bmi=form1.cleaned_data['bmi']
			age=form1.cleaned_data['age']
			diabetes_pedigree_function=form1.cleaned_data['diabetes_pedigree_function']
			
			pred = mlp(glucose,insulin,blood_pressure,skin_thickness,pregnancies,bmi,age,diabetes_pedigree_function)
			args = {'form1' : form1, 'pred' : pred}
			form1=DataForm()
			
		return render(request,self.template_name,args)		

#for training:
def model_form_train(request):
	if request.method == 'POST':
		form2=DocumentForm(request.POST, request.FILES)
		if form2.is_valid():
			form2.save()
			csv_file=request.FILES['document']
			if not csv_file.name.endswith('.csv'):
				messages.error(request,'File is not csv type')
				return render(request, "training.html" ,{'form2' : form2})
			file=csv_file.name
			
			accuracy = mlp_csv(file)
			accuracy = accuracy*100
			return render(request, "training.html" ,{'form2' : form2, 'accuracy' : accuracy})
	else:
		form2=DocumentForm(request.POST, request.FILES)
		return render(request, "training.html" ,{'form2' : form2})


    
def get_image(request):
	r=graph('finalized_model_dt.sav')
	return r    
    
    