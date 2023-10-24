from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

#1
dataset_train = pd.read_csv('milk_training.csv') #pilih file csv
train_data = np.array(dataset_train)[:, 0:-1]
train_label = np.array(dataset_train)[:,-1]

#2
dataset_test = pd.read_csv('milk_testing.csv') #pilih file csv

test_data = np.array(dataset_test)[:, 0:-1]
test_label = np.array(dataset_test)[:,-1]

#3
#GNB
gnb_train = GaussianNB()
gnb_train.fit(train_data, train_label)

#MNB
mnb_train = MultinomialNB(force_alpha=True)
mnb_train.fit(train_data, train_label)

#BNB
bnb_train = BernoulliNB(force_alpha=True)
bnb_train.fit(train_data, train_label)

hasil_gnb_before = gnb_train.predict(test_data)
hasil_mnb_before = mnb_train.predict(test_data)
hasil_bnb_before = bnb_train.predict(test_data)

score_gnb_before = accuracy_score(test_label, hasil_gnb_before)
score_mnb_before = accuracy_score(test_label, hasil_mnb_before)
score_bnb_before = accuracy_score(test_label, hasil_bnb_before)

print('= Before =======================================================================')
print('Nilai akurasi GNB: ',score_gnb_before)
print('================================================================================')

print('Nilai akurasi MNB: ',score_mnb_before)
print('================================================================================')

print('Nilai akurasi BNB: ',score_bnb_before)
print('================================================================================\n')

#4
max_element_column = np.max(train_data, 0)
min_element_column = np.min(train_data, 0)
newmin = 0
newmax = 1
train_data_scaled = ((train_data - min_element_column)*(newmax - newmin)/(max_element_column - min_element_column)) + newmin
test_data_scaled = ((test_data - min_element_column)*(newmax - newmin)/(max_element_column - min_element_column)) + newmin

#5
gnb_train.fit(train_data_scaled, train_label)
mnb_train.fit(train_data_scaled, train_label)
bnb_train.fit(train_data_scaled, train_label)

hasil_gnb = gnb_train.predict(test_data)
hasil_mnb = mnb_train.predict(test_data)
hasil_bnb = bnb_train.predict(test_data)

#6
score_gnb = accuracy_score(test_label, hasil_gnb)
score_mnb = accuracy_score(test_label, hasil_mnb)
score_bnb = accuracy_score(test_label, hasil_bnb)

#7

print('= After ========================================================================')
print('Nilai akurasi GNB: ',score_gnb)
print('================================================================================')

print('Nilai akurasi MNB: ',score_mnb)
print('================================================================================')

print('Nilai akurasi BNB: ',score_bnb)
print('================================================================================')