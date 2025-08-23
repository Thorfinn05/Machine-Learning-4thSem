with open ("D:\Github\Machine-Learning-4thSem\Movie Review.txt") as file:
    review = file.read()
    print(review)
review = review.lower()
words = review.split()
print(words)
modified_review = words

punctuations = [",", ".", "?"]
positive_words = ["sure", "enjoyable", "great", "nice", "good", "fantastic", "wow", "charming"]
negative_words = ["second-grade", "hokey", "bad", "boring", "break-up", "worthless"]
pronouns = ['i', "me", "you", "they", "we", "he", "she", "them"]

features = []
x1 =0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0

for word in words:
    x6 += 1
print(x6)

for word in words:
    if word in punctuations:
        words.remove(word)
print(modified_review)

for word in modified_review:
    if word in positive_words:
        x1 += 1
    elif word in negative_words:
        x2 += 1
    elif word in pronouns:
        x4 += 1
    elif (word == "no"):
        x3 += 1
    elif (word == "!"):
        x5 += 1
