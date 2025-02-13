# -------------------------------------------------------------------------
# AUTHOR: Huynh Pham
# FILENAME: decision_tree.py
# SPECIFICATION:
"""
This program predicts whether a person should wear contact lenses or not using a decision tree. 
The program reads data from a CSV file, converts words to numbers, 
trains a decision tree, and then displays the tree as a diagram.
"""
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 week
# -----------------------------------------------------------*/

# IMPORTANT NOT: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []

# reading the data in a csv file
with open("contact_lens.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# --> add your Python code here
# X =
# Encoding categorical features into numbers
age_map = {"Young": 1, "Prepresbyopic": 2, "Presbyopic": 3}
spectacle_map = {"Myope": 1, "Hypermetrope": 2}
astigmatism_map = {"Yes": 1, "No": 2}
tear_map = {"Normal": 1, "Reduced": 2}
class_map = {"Yes": 1, "No": 2}

# Transforming data
for row in db:
    X.append(
        [
            age_map[row[0]],
            spectacle_map[row[1]],
            astigmatism_map[row[2]],
            tear_map[row[3]],
        ]
    )

# transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
# --> add your Python code here
# Y =
for row in db:
    Y.append(class_map[row[4]])

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(
    clf,
    feature_names=["Age", "Spectacle", "Astigmatism", "Tear"],
    class_names=["Yes", "No"],
    filled=True,
    rounded=True,
)
plt.show()
