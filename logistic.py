with open ("D:\Github\Machine-Learning-4thSem\Movie Review.txt") as file:
    review = file.read()
    print(review)
review = review.lower()
words = review.split()
print(words)
x6 = 0
for word in words:
    x6 += 1
print(x6)