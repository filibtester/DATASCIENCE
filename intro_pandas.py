
# coding: utf-8

# # Importing libraries and the data set:

import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")   # Reading the dataset in a dataframe 

# # Quick Data Exploration

df.head()
df.describe()   # Get summary of numerical data

# LoanAmount has (614 - 592) 22 missing values. 
# Loan_Amount_Term has (614 - 600) 14 missing values.
# Credit_History has (614 - 564) 50 missing values.
# 84% of the applicants have a credit_history because the mean is 0.84.

df['Property_Area'].value_counts()   # Indexing technique

# # Distribution Analysis

df['ApplicantIncome'].hist(bins=50)

# There are few extreme values. Let's look at box plots to understand the distributions.

df.boxplot(column='ApplicantIncome')

# boxplot confirms the presence of a lot of outliers/extreme values. Let's see if Educations matters:

df.boxplot(column='ApplicantIncome', by = 'Education')


# The mean seems to be the same for Graduate and Not Graduate but there are Applicants with 
# high Income in Graduates. Let's see in Gender matters.

df.boxplot(column='ApplicantIncome', by = 'Gender')

# Males have extreme values. Let's have a look at the histogram and boxplot of LoanAmount.

df['LoanAmount'].hist(bins=50)

df.boxplot(column='LoanAmount')


# There are extreme values also in LoanAmount, like in ApplicantIncome. We have to do some data munging.

# # Categorical Variable Analysis

temp1 = df['Credit_History'].value_counts(ascending=True)
print ('Frequency Table for Credit History: ')
temp1

temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print('\nProbability of getting loan for each Credit History class: ')
temp2

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')


ax2 = fig.add_subplot(122)
temp2.plot(kind='bar')
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by credit history")


# The chances of getting a loan are eight-fold if the applicant has a valid credit history. Let's do the same for Married

temp3 = df['Married'].value_counts(ascending=True)
temp3

temp4 = df.pivot_table(values='Loan_Status',index=['Married'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print('\nProbability of getting loan for each Married: ')
temp4

fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Married')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Married")
temp3.plot(kind='bar')


ax2 = fig.add_subplot(122)
temp4.plot(kind='bar')
ax2.set_xlabel('Married')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by Married")

temp5 = pd.crosstab(df['Credit_History'], df['Loan_Status'])
temp5.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)


temp6 = pd.crosstab(df['Gender'], df['Loan_Status'])
temp6.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)

