import math

def sigmoid(z):
    result = 1/(1+(2.718**(-z)))
    return result

def loss_function(y, yg):
    result = -(yg*math.log(y) + ((1-yg)*math.log(1-y)))
    return result

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
x6 = math.log(x6)

print("Positive words: ", x1)
print("Negative words: ", x2)
print("Number of no: ", x3)
print("Number of Prononuns: ", x4)
print("Number of Excalimation: ", x5)
print("Number of words(log): ", x6)

features.append(x1)
features.append(x2)
features.append(x3)
features.append(x4)
features.append(x5)
features.append(x6)
print("Features: \n", features)

weights = [2.5, -5.0, -1.2, 0.5, 2.0, 0.7]
bias = 0.1
z = 0

for i in range(len(features)):
    z = z + weights[i]*features[i]
z = z + bias
print("The value of Z: ", z)

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
