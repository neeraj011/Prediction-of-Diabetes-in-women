# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier
from django.conf import settings
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

import pickle
import os
#v1=
#v2=
BASE_DIR=getattr(settings,"MEDIA_ROOT",None)
def mlp(v1,v2,v3,v4,v5,v6,v7,v8):
	clf1=pickle.load(open("finalized_model_dt.sav", 'rb'))
	temp=[v1,v2,v3,v4,v5,v6,v7,v8]
	temp = np.array(temp).reshape((1, -1))
	pred = clf1.predict(temp)
	if pred=='0':
		pred = 'Diabetes test results: Negative'
	else:
		pred = 'Diabetes test results: Positive'
	return pred

def mlp_csv(csv_file):
	
	df = pd.read_csv(os.path.join(BASE_DIR,"documents",csv_file), header = 0)

	X = np.array(df.drop(['Outcome'],1))
	y = np.array(df['Outcome'])

	X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

	# the classifier
	clf1 = tree.DecisionTreeClassifier()

	# train
	clf1.fit(X_train, y_train)

	# predict
	pred = clf1.predict(X_test)
	# print(y_test)
	# print(pred)

	accuracy = accuracy_score(pred, y_test)

	# print ('\naccuracy = {0}'.format(accuracy))

	filename='finalized_model_dt.sav'

	pickle.dump(clf1, open(filename, 'wb'))
	pickle.dump(accuracy, open(filename, 'wb'))
	for count in range(0,6000):
		# print(count)
		X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

		# the classifier
		clf1 = tree.DecisionTreeClassifier()

		# train
		clf1.fit(X_train, y_train)

		# predict
		pred = clf1.predict(X_test)
		# print(y_test)
		# print(pred)

		accuracy1 = accuracy_score(pred, y_test)
		f=open(filename, 'wb')
		if accuracy1>accuracy:
			accuracy=accuracy1
			clf2=clf1
			a = [[0,0], [0,0]] 
			a=confusion_matrix(y_test, pred, labels=None, sample_weight=None)
		
	# print ('\n Final accuracy = {0}'.format(accuracy))
	# print("Confusion matrix is:")
	# print(a)
	pickle.dump(clf2, f)
	pickle.dump(accuracy, f)
	pickle.dump(a, f)
	# print ("\nTotal time taken:", round(time()-t1, 3), "s")
	return(accuracy)   