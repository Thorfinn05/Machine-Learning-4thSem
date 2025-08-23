with open ("D:\Github\Machine-Learning-4thSem\Movie Review.txt") as file:
    review = file.read()
    print(review)
review = review.lower()
words = review.split()
print(words)