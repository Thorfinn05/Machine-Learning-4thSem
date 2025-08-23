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

x6 = 0

for word in words:
    x6 += 1
print(x6)

for word in words:
    if word in punctuations:
        words.remove(word)
print(modified_review)