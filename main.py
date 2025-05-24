import string

# Load positive words
with open("positive_words.txt", "r") as f:
    positive_words = [line.strip() for line in f if line.strip()]

# Sample reviews
reviews = [
    "I absolutely loved this product! It's amazing and so helpful.",
    "Not what I expected. Quite disappointing and bad.",
    "Okay product, works fine but nothing special.",
    "Fantastic quality and excellent customer support!",
    "Terrible. Waste of money. Do not buy."
]

# Cleaning and sentiment functions
def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    return text.split()

def count_positive_words(words, positive_words):
    return sum(1 for word in words if word in positive_words)

def label_sentiment(review, positive_words):
    words = clean_text(review)
    count = count_positive_words(words, positive_words)
    return "Positive" if count >= 2 else "Negative"

# Run sentiment analysis
for review in reviews:
    sentiment = label_sentiment(review, positive_words)
    print(f"Review: {review}\nSentiment: {sentiment}\n")
