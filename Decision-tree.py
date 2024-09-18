import pandas as pd                                                                   # Import necessary libraries

                                                                                    # Define the column names manually
column_names = ['Alternate', 'Bar', 'Fri/Sat', 'Hungry', 'Patrons', 'Price','Raining', 'Reservation', 'Type', 'WaitEstimate', 'Wait']
data = pd.read_csv('restaurant.csv', header=None, names=column_names)                  # Load the dataset without a header


print("First few rows of the dataset:")                                               # Print the first few rows of the dataset to ensure it's loaded correctly
print(data.head())


X = data.drop('Wait', axis=1)                                                      # Split the data into features (X) and target (y)
y = data['Wait']
X = pd.get_dummies(X)                                                              # Convert categorical variables to numerical using get_dummies


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)      # Split the data into training and testing sets (80% train, 20% test)
from sklearn.tree import DecisionTreeClassifier


clf = DecisionTreeClassifier(random_state=42)                                     # Train the Decision Tree Classifier
clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report
y_pred = clf.predict(X_test)                                                       # Predict the test set results
accuracy = accuracy_score(y_test, y_pred)                                         # Calculate the accuracy of the model
print(f"Accuracy: {accuracy * 100:.2f}%")


print("Classification Report:")                                                  # Generate a classification report
print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


plt.figure(figsize=(20,10))                                                         # Plot the Decision Tree
plot_tree(clf, feature_names=X.columns, class_names=True, filled=True)
plt.show()

feature_importances = clf.feature_importances_                                       # Get the feature importances
features_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances}) # Create a DataFrame for better visualization of feature importances                                                                               
features_df = features_df.sort_values(by='Importance', ascending=False)               # Sort the DataFrame by importance


plt.figure(figsize=(10, 6))                                                              # Plot the feature importances
plt.barh(features_df['Feature'], features_df['Importance'], color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance in Decision Tree')
plt.gca().invert_yaxis()                                                             # To display the most important feature at the top
plt.show()

