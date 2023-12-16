#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
emp_data = pd.read_csv('Data/HR_comma_sep.csv.txt')
emp_data.head()
emp_data.rename(columns={'sales':'dept'}, inplace=True)
emp_data.head()

import numpy as np
import pandas as pd
import seaborn as sns; sns.set(color_codes=True)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

emp_data.describe()
emp_data.select_dtypes('object').columns
emp_data.dept.value_counts()
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()
dept = le.fit_transform(emp_data.dept)
ohe = OneHotEncoder()
ohe_dept = ohe.fit_transform(dept.reshape(-1,1))
ohe.active_features_
le.classes_
dept_df = pd.DataFrame(ohe_dept.toarray(), dtype=int,columns=le.classes_)
emp_data['salary_tf'] = emp_data.salary.map({'low':1,'medium':2,'high':3})
from sklearn.preprocessing import StandardScaler,MinMaxScaler
emp_data.columns
df = emp_data[['number_project','average_montly_hours', 'time_spend_company']]
df.plot.kde()
mm = MinMaxScaler()
scaled_np = mm.fit_transform(df)
dept_np = dept_df.values
emp_df = emp_data[['satisfaction_level','last_evaluation','Work_accident','promotion_last_5years','salary_tf']]
emp_np = emp_df.values
feature_data = np.hstack([emp_np, scaled_np, dept_np])
target_data = emp_data.left
feature_data.shape
target_data.value_counts()
from sklearn.linear_model import LogisticRegression, SGDClassifier, PassiveAggressiveClassifier
from sklearn.ensemble import RandomForestClassifier
models = [ LogisticRegression(class_weight='balanced'), SGDClassifier(max_iter=10), PassiveAggressiveClassifier(max_iter=20), RandomForestClassifier(n_estimators=20)]
from sklearn.model_selection import train_test_split
trainX,testX,trainY,testY = train_test_split(feature_data,target_data)
for model in models:

    model.fit(trainX,trainY)

    print (model.score(testX,testY))


# In[ ]:




