import numpy as np
from tensorflow import keras

import project_types as GLOB



class Brain_Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Brain_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class Brain(object, metaclass=Brain_Singleton):


    def __init__(self
        ):
        self._DIRECTIONS_NUMBER = 8
        len = GLOB.PET_VIEW_DIAMETER
        self._net = keras.Sequential()
        self._net.add(keras.layers.Flatten(input_shape=(len, len)),)
        self._net.add(keras.layers.Dense(10, activation='relu'))
        self._net.add(keras.layers.Dense(10, activation='relu'))
        self._net.add(keras.layers.Dense(self._DIRECTIONS_NUMBER, activation='softmax'))
        self._net.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])


    def calculate_direction(self,
        visible_area # np 2-d matrix
        ):
        area_3d = visible_area.reshape((1, GLOB.PET_VIEW_DIAMETER, GLOB.PET_VIEW_DIAMETER))
        directions = self._net.predict(area_3d)

        return np.argmax(directions)


    def train(self,
        history # array of dicts: [{"areas", "directions"}]
        ):
        lifes_lengths = self._calc_lifes_parameters(history)
        X = None
        Y = None

        for pet_history in history:
            if len(pet_history["areas"]) < lifes_lengths["max_length"]:
                continue
            (x, y) = self._build_train_batch(pet_history, lifes_lengths)
            X = x if X is None else np.vstack((X, x))
            Y = y if Y is None else np.vstack((Y, y))

        self._net.fit(X, Y, epochs=5, verbose=0)

        return lifes_lengths


    def _build_result_sample(self,
        lifes_lengths,
        pet_life_length,
        direction,
        y
        ):
        if lifes_lengths["min_length"] == lifes_lengths["max_length"]:
            y.fill(1 / self._DIRECTIONS_NUMBER)
            return

        max_len = lifes_lengths["max_length"]
        min_len = lifes_lengths["min_length"]
        aver_len = lifes_lengths["average_length"]
        n = self._DIRECTIONS_NUMBER

        if pet_life_length < aver_len:
            koef = 1 - (aver_len - pet_life_length) / (aver_len - min_len)
            true_value = koef * 1 / n
        else:
            koef = (pet_life_length - aver_len) / (max_len - aver_len)
            true_value = koef * (1 - 1 / n) + 1 / n

        false_value = (1 - true_value) / (n - 1)

        if aver_len <= pet_life_length:
            false_value = 0
            true_value = 1

        y.fill(false_value)
        y[0, direction] = true_value


    def _build_train_batch(self,
        pet_history, # dict: {"areas", "directions"}
        lifes_lengths # dict: {"min_length", "average_length", "max_length"}
        ):
        X = None
        Y = None
        pet_life_length = len(pet_history["areas"])

        for i in range(pet_life_length):
            x = pet_history["areas"][i].reshape((1, GLOB.PET_VIEW_DIAMETER, GLOB.PET_VIEW_DIAMETER))
            y = np.zeros((1, self._DIRECTIONS_NUMBER))
            direction = pet_history["directions"][i]
            self._build_result_sample(lifes_lengths, pet_life_length, direction, y)
            # if X is None:
            #     X = x.copy()
            # else:
            #     X = np.hstack((X, x))
            X = x.copy() if X is None else np.vstack([X, x])
            Y = y.copy() if Y is None else np.vstack([Y, y])

        return (X, Y)


    def _calc_lifes_parameters(self,
        history # array of dicts: [{"areas", "directions"}]
        ):
        min_length = 1000000
        max_length = 0
        total_lenght = 0

        for pet_history in history:
            curr_length = len(pet_history["areas"])
            total_lenght += curr_length
            min_length = min(min_length, curr_length)
            max_length = max(max_length, curr_length)

        return {"min_length": min_length,
                "average_length": total_lenght / len(history),
                "max_length": max_length}


