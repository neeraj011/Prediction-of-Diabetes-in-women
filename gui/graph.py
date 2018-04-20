import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import io
from django.http import HttpResponse


def graph(file):
	f=open(file, 'rb')
	cl_dt=pickle.load(f)
	accuracy_dt=pickle.load(f)
	a=pickle.load(f)

	labels = 'Right', 'Wrong'
	sizes = [a[0][0],a[0][1]]
	colors = ['#0000FF', '#58D3F7']
	explode = (0, 0)
	ax=plt.subplot(131)
	plt.rcParams['font.size'] = 9.0
	ax.set_title('Non-diabetic females')
	ttl=ax.title
	ttl.set_position([0.5,0.7])
	plt.axis('equal')
	plt.rcParams['font.size'] = 7.0
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.0f%%', shadow=False, startangle=140)

	labels = 'Right', 'Wrong'
	sizes = [a[1][1],a[1][0]]
	colors = ['#0000FF', '#58D3F7']
	explode = (0, 0)
	ax=plt.subplot(132)
	plt.rcParams['font.size'] = 9.0
	ax.set_title('Diabetic females')
	ttl=ax.title
	ttl.set_position([0.5,0.7])
	plt.axis('equal')
	plt.rcParams['font.size'] = 7.0
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.0f%%', shadow=False, startangle=140)

	labels = 'Accuracy', ''
	sizes = [accuracy_dt,1-accuracy_dt]
	colors = ['#0000FF', '#58D3F7']
	explode = (0, 0)  # explode 1st slice
	# Plot
	ax=plt.subplot(133)
	plt.rcParams['font.size'] = 9.0
	ax.set_title('Total Accuracy')
	ttl=ax.title
	ttl.set_position([0.5,0.7])
	plt.axis('equal')
	plt.rcParams['font.size'] = 7.0
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%0.4f%%', shadow=False, startangle=140)

	f1 = io.BytesIO()
	plt.savefig(f1, format='png')
	plt.clf()
    	#plt.show()
	return HttpResponse(f1.getvalue(), content_type='image/png')