from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    if polarity > 0.1:
        interpretation = "Positive"
    elif polarity < -0.1:
        interpretation = "Negative"
    else:
        interpretation = "Neutral"

    return {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "interpretation": interpretation,
    }