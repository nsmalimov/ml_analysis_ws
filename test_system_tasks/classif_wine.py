from sklearn.cross_validation import train_test_split


def prepare_data():
    data = []
    f = open("/Users/Nurislam/PycharmProjects/diplom_ml_platform/test_system_tasks/datasets/wine.csv", "r")

    for i in f.readlines():
        s = i.replace("\n", "")
        s_split = s.split(",")
        s_new = ",".join(s_split[1:]) + "," + s_split[0]
        data.append(s_new)
    f.close()

    f = open("/Users/Nurislam/PycharmProjects/diplom_ml_platform/test_system_tasks/datasets/wine.csv", "w")

    for i in data:
        f.write(i + "\n")
    f.close()

#prepare_data()

X, Y = [], []

f = open("/Users/Nurislam/PycharmProjects/diplom_ml_platform/test/data/wine.csv", "r")

for i in f.readlines():
    s = i.replace("\n", "")
    s_split = s.split(",")

    X.append([float(i) for i in s_split[:-1]])
    Y.append(s_split[-1])

f.close()

import ml_data.common_algorithms.random_forest

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
print (len(X_test))
print (len(X_train))
model = ml_data.common_algorithms.random_forest.train(X_train, Y_train)
#print (model)
print (model.score(X_test, Y_test))

import ml_data.common_algorithms.log_reg

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
model1 = ml_data.common_algorithms.log_reg.train(X_train, Y_train)
#print (model1)
print (model1.score(X_test, Y_test))
#metrics1, plots1 = test(model1, X, Y)


import ml_data.common_algorithms.svm

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
model2 = ml_data.common_algorithms.svm.train(X_train, Y_train)
#print (model2)
print (model2.score(X_test, Y_test))
#metrics2, plots2 = test(model2, X, Y)

import test.data.random_algorithm

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
model3 = test.data.random_algorithm.train(X_train, Y_train)
#print (model2)
print (test.data.random_algorithm.test(model3, X_test, Y_test))
