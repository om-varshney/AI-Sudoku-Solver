import tensorflow as tf


class AccuracyBarrier(tf.keras.callbacks.Callback):
    def __init__(self, accuracy_barrier=0.6):
        super().__init__()
        self.accuracy_barrier = accuracy_barrier

    def on_epoch_end(self, epoch, logs=None):
        if logs.get('accuracy') >= self.accuracy_barrier:
            print(f"Training abort, desired accuracy reached- {self.accuracy_barrier}")
            self.model.stop_training = True
