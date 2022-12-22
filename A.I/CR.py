import sys
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QWidget
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.initUI()

    def initUI(self):
        # Create the input and output fields
        input_label = QLabel("Input:")
        self.input_field = QLineEdit()
        output_label = QLabel("Output:")
        self.output_field = QTextEdit()

        # Create the "Run" button
        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run_code)

        # Add the widgets to a grid layout
        grid = QGridLayout()
        grid.addWidget(input_label, 0, 0)
        grid.addWidget(self.input_field, 0, 1)
        grid.addWidget(output_label, 1, 0)
        grid.addWidget(self.output_field, 1, 1)
        grid.addWidget(run_button, 2, 1, Qt.AlignRight)

        self.setLayout(grid)

        # Set the window properties
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("TensorFlow GUI")

    def run_code(self):
        # Load the data
        questions = [
            "Hi",
            "What is your name?",
            "How old are you?",
            "Where are you from?",
            "What do you do?",
            "What are your hobbies?",
        ]

        answers = [
            "Hello",
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

            return (x_train, y_train), (x_val, y_val)

        # Load and preprocess the data

        (x_train, y_train), (x_val, y_val) = self.load_and_preprocess_data()
    
        # Build the model
    inputs = tf.keras.Input(shape=(None,), dtype=tf.int32)
    embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)(inputs)
    encoder_outputs, state_h, state_c = tf.keras.layers.LSTM(encoder_units, return_state=True)(embeddings)
    encoder_states = [state_h, state_c]
    
    decoder_inputs = tf.keras.Input(shape=(None,), dtype=tf.int32)
    decoder_embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)(decoder_inputs)
    decoder_lstm = tf.keras.layers.LSTM(decoder_units, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_embeddings, initial_state=encoder_states)
    decoder_dense = tf.keras.layers.Dense(vocab_size, activation='softmax')
    outputs = decoder_dense(decoder_outputs)
    
    model = tf.keras.Model([inputs, decoder_inputs], outputs)
    
    # Compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # Train the model
    history = model.fit([x_train, y_train[:, :-1]], y_train[:, 1:], batch_size=32, epochs=10, validation_data=([x_val, y_val[:, :-1]], y_val[:, 1:]))
    
    # Evaluate the model
    val_loss, val_acc = model.evaluate([x_val, y_val[:, :-1]], y_val[:, 1:])

    print("Validation loss:", val_loss)
    print("Validation accuracy:", val_acc)

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper left')
    plt.show()

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper left')
    plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
