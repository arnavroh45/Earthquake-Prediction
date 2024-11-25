import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC

# Load and preprocess the dataset
data = pd.read_csv("dataset.csv")
data = np.array(data)
X = data[:, 0:-1]
y = data[:, -1]
y = y.astype('int')
X = X.astype('int')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Use SVM classifier with RBF kernel
svm = SVC(kernel='rbf')  # You can replace 'rbf' with 'linear', 'poly', or 'sigmoid' for different kernels
svm.fit(X_train, y_train)

# Make predictions
y_pred = svm.predict(X_test)

# Print accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Save the model if needed
# pickle.dump(svm, open('model.pkl', 'wb'))
