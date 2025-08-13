positive_words = {"good", "great", "amazing", "enjoyable", "nice", "fantastic", "love", "excellent", "wonderful", "best"}
negative_words = {"bad", "worst", "boring", "terrible", "awful", "poor", "hate", "2nd grade", "waste", "disappointing"}
pronouns = {"I", "me", "my", "you", "your"}

review_text = input ("Enter a review: ")
x1, x2, x3, x4, x5, x6 = analyze_review(review_text)

print("\n Feature values: ");
print("\n x1(Positive words): ",x1, 
      "\n x2 (Negative words): ",x2, 
      "\n x3 (Contains 'no'): ",x3, 
      "\n x4 (Prononun Counts): ",x4, 
      "\n x5 (Exclamation marks): ",x5, 
      "\n x6 Total words): ",x6)