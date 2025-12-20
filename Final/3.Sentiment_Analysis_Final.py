import math

def sigmoid(z):
    return 1/(1 + (2.718 ** (-z)))

def loss_function(y, yg):
    result = -(yg * math.log(y) + ((1-yg) * math.log(1-y)))
    return result

with open("D:\Github\Machine-Learning-4thSem\Movie Review.txt") as file:
    review = file.read()
    print(review)
review = review.lower()
words_modified = review.split()
print(words_modified)

punctuations = [".", ",", "?"]
positive_words = ["sure", "enjoyable", "great", "nice", "good", "fantastic", "wow", "charming"]
negative_words = ["second-grade", "hokey", "bad", "boring", "break-up", "worthless"]
pronouns = ['i', "me", "you", "they", "we", "he", "she", "them"]

for word in words_modified:
    if word in punctuations:
        words_modified.remove(word)

features = [0,0,0,0,0,0]

for word in words_modified:
    features[5] += 1
    if word in positive_words:
        features[0] += 1
    elif word in negative_words:
        features[1] += 1
    elif word in pronouns:
        features[3] += 1
    elif (word == "no"):
        features[2] += 1
    elif (word == "!"):
        features[4] += 1
features[5] = math.log(features[5])

print("Positive words: ", features[0])
print("Negative words: ", features[1])
print("Number of no: ", features[2])
print("Number of Prononuns: ", features[3])
print("Number of Excalimation: ", features[4])
print("Number of words(log): ", features[5])

weights = [2.5, -5.0, -1.2, 0.5, 2.0, 0.7]
bias = 0.1
z = 0

for i in range(len(features)):
    z = z + (weights[i] * features[i])
z = z + bias

sigmoid_value = sigmoid(z)
print("Sigmoid Value: ", sigmoid_value)

if (sigmoid_value <= 0.5):
    print("The review is negative!")
else:
    print("The review is positive!")

positive_loss = loss_function(sigmoid_value, 1)
negative_loss = loss_function(sigmoid_value, 0)

print("The positive loss is: ", positive_loss)
print("The negative loss is: ", negative_loss)