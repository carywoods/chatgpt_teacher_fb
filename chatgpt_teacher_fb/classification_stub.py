from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# Assuming 'cleaned_data' is a pandas DataFrame with 'text' and 'category' columns
texts = cleaned_data['ONE SENTENCE DESCRIPTION']
categories = cleaned_data['Category']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, categories, test_size=0.2, random_state=42)

# Create a pipeline that transforms the data to a TF-IDF vector and then applies a Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Predict the categories for the testing set
predicted_categories = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, predicted_categories))
