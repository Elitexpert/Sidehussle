import numpy as np

# Load the data
questions = [
     "What is your name?",
     "How old are you?",
     "Where are you from?",
    "What do you do?",
    "What are your hobbies?",
    ]

answers = [
     "My name is Alice.",
     "I am 25 years old.",
     "I am from New York.",
     "I am a software engineer.",
      "I enjoy reading, hiking, and playing video games.",
    ]

# Preprocess the data
def load_and_preprocess_data():
    vocab = set(questions + answers)
    vocab_size = len(vocab)

# Create a vocabulary index
    vocab_index = {word: index for index, word in enumerate(vocab)}

# Encode the data
    def encode(sentence):
        encoded_sentence = []
        for word in sentence.split():
            if word in vocab_index:
             encoded_sentence.append(vocab_index[word])
        return encoded_sentence

    x_train = np.array([encode(question) for question in questions])
    y_train = np.array([encode(answer) for answer in answers])

# Create a validation set
    x_val = x_train[:2]
    y_val = y_train[:2]

# Use the remaining data for training
    x_train = x_train[2:]
    y_train = y_train[2:]
