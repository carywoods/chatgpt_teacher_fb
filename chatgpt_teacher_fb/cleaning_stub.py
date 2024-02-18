# Example of sentiment analysis code
from textblob import TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'

# Example of high-engagement posts analysis
likes_75th_percentile = cleaned_data['NUMBER OF LIKES'].quantile(0.75)
high_engagement_posts = cleaned_data[cleaned_data['NUMBER OF LIKES'] > likes_75th_percentile]
