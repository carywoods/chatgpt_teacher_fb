from textblob import TextBlob

def analyze_sentiment(text):
    """
    This function takes a string input (text) and returns the sentiment analysis results,
    including the polarity and subjectivity scores. It utilizes the TextBlob library,
    which is built on top of NLTK and Pattern libraries, to perform the sentiment analysis.
    
    Parameters:
    - text (str): The text to be analyzed.
    
    Returns:
    - sentiment (str): The overall sentiment ('Positive', 'Neutral', 'Negative').
    - polarity (float): A float within the range [-1.0, 1.0] where 1 means positive statement and -1 means a negative statement.
    - subjectivity (float): A float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, polarity, subjectivity

# Example usage
text_example = "ChatGPT is an amazing tool for educators, providing immense value in creating interactive learning experiences."
sentiment, polarity, subjectivity = analyze_sentiment(text_example)
print(f"Sentiment: {sentiment}, Polarity: {polarity}, Subjectivity: {subjectivity}")
