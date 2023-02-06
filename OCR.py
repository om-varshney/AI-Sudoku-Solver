"""
This file will contain our model which will be used to recognise the digits.
We will modify the dataset so that empty boxes will be recognised as zeros.
"""
import numpy as np
import tensorflow as tf
from callbacks import AccuracyBarrier
import os

if not os.path.isfile("Models/ocr_high_accuracy.h5"):
    # load the mnist dataset
    mnist = tf.keras.datasets.mnist

    # split the data into testing and training sets.
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data()

    # Normalise the values
    training_images = training_images / 255
    test_images = test_images / 255

    # Invert the pictures
    training_images = (training_images - 1) * -1
    test_images = (test_images - 1) * -1

    # Transform all zeroes to empty cells
    training_images[training_labels == 0] = np.ones([28, 28])
    test_images[test_labels == 0] = np.ones([28, 28])

    training_images = training_images.reshape(60000, 28, 28, 1)
    test_images = test_images.reshape(10000, 28, 28, 1)

    # Define our CNN
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu, input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax),
        # tf.keras.layers.Conv2D(64, 7, activation="relu", padding="same", input_shape=[28, 28, 1]),
        # tf.keras.layers.MaxPooling2D(2),
        # tf.keras.layers.Conv2D(128, 3, activation="relu", padding="same"),
        # tf.keras.layers.Conv2D(128, 3, activation="relu", padding="same"),
        # tf.keras.layers.MaxPooling2D(2),
        # tf.keras.layers.Conv2D(256, 3, activation="relu", padding="same"),
        # tf.keras.layers.Conv2D(256, 3, activation="relu", padding="same"),
        # tf.keras.layers.MaxPooling2D(2),
        # tf.keras.layers.Flatten(),
        # tf.keras.layers.Dense(128, activation="relu"),
        # tf.keras.layers.Dropout(0.5),
        # tf.keras.layers.Dense(64, activation="relu"),
        # tf.keras.layers.Dropout(0.5),
        # tf.keras.layers.Dense(10, activation="softmax")
    ])
    # Now we shall compile our model
    model.compile(
        optimizer=tf.optimizers.Adam(),
        loss='sparse_categorical_crossentropy',
        metrics=[
            'accuracy',
        ],
    )
    # instantiating our callback
    accuracy_barrier = AccuracyBarrier(0.9998)
    history = model.fit(
        training_images,
        training_labels,
        epochs=40,
        callbacks=[
            accuracy_barrier,
        ],
    )
    model.save("./ocr_high_accuracy.h5")
    # Now we will evaluate our model
    model.evaluate(test_images, test_labels)
