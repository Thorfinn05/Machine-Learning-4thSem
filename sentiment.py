positive_words = {"good", "great", "amazing", "enjoyable", "nice", "fantastic", "love", "excellent", "wonderful", "best"}
negative_words = {"bad", "worst", "boring", "terrible", "awful", "poor", "hate", "2nd grade", "waste", "disappointing"}
pronouns = {"I", "me", "my", "you", "your"}

def analyze_review(review):
    review_lower = review.lower()
    words = review_lower.split()

    pos_count  = 0
    neg_count = 0
    pronoun_count = 0
    contains_no = 1 if "no" in words else 0
    exclamation_count = review.count("!")
    total_words = len(words)

    for word in words:
        word_clean = word.split(". , ! ?")
        if word_clean in positive_words:
            pos_count += 1
        elif word_clean in negative_words:
            neg_count += 1
        elif word_clean in pronouns:
            pronoun_count += 1
    return pos_count, neg_count, contains_no, pronoun_count, exclamation_count, total_words

review_text = input ("Enter a review: ")
x1, x2, x3, x4, x5, x6 = analyze_review(review_text)

print("\n Feature values: ")
print("\n x1(Positive words): ",x1, 
      "\n x2 (Negative words): ",x2, 
      "\n x3 (Contains 'no'): ",x3, 
      "\n x4 (Prononun Counts): ",x4, 
      "\n x5 (Exclamation marks): ",x5, 
      "\n x6 Total words): ",x6)