

import numpy as np
from copy import deepcopy

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.losses import BinaryCrossentropy

class FFNNPeasant(object):
    
    def __init__(self, **kwargs):
        """ FFNNPeasant is a simple FFNN class to train and compute output.
        The DNA serves as the reference to build the layers and neurons.
        """
        
        self.__kwargs = deepcopy(kwargs)
        self.__dna_features = self.__kwargs["dna_features"]
        self.__ref_ffnn = self.__dna_features["ref"]
        
        self.__dna = self.__kwargs.get("dna", self.__random_initilization())
        self.__model = self.__generate_model()
        self.__model.compile(optimizer = 'adam',
                             loss = BinaryCrossentropy())
        self.__fitness = None
    
    @property
    def dna(self):
        return deepcopy(self.__dna)
    
    @property
    def dna_features(self):
        return deepcopy(self.__dna_features)
        
    @property
    def fitness(self):
        return self.__fitness
    
    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    
    def __generate_model(self):
        """Generate FFNN model from the DNA

        Returns
        -------
        Keras Model
            Sequential Model with the layers
        """
        
        layers = []
        for eg, gene in enumerate(self.__dna):
            units = self.__ref_ffnn[int(gene)]
            if units == 0:
                continue
            
            dense = None
            if eg == 0:
                dense = Dense(units = units, input_shape = (1,),
                              activation = 'relu', name = f'layer_{eg}')
            else:
                dense = Dense(units = units, activation = 'relu', name = f'layer_{eg}')
                
            layers.append(dense)
            
        layers.append(Dense(units = 1, activation = 'sigmoid', name = f'layer_{eg+1}'))
        model = Sequential(layers)
        
        return model
        
    def __random_initilization(self):
        """Function to initialize the FFNNPeasant with random DNA

        Returns
        -------
        str
            DNA of this FFNNPeasant
        """
        
        dna_length = self.__dna_features["length"]
        dna = "".join(str(jj) for jj in np.random.choice(len(self.__ref_ffnn), dna_length))
        
        return dna
    
    
    def fit_model(self, _input, _output):
        """Fit the model

        Parameters
        ----------
        _input : np.ndarray
            Input values for training the model
        _output : np.ndarray
            Output values for training the model
        """
        
        callback = EarlyStopping(monitor = 'loss', mode = 'min', start_from_epoch = 10,
                                 patience = 5, verbose = 0)
        history = self.__model.fit(x = tf.convert_to_tensor(_input, dtype = tf.float32),
                                   y = tf.convert_to_tensor(_output, dtype = tf.float32),
                                   validation_split = 0.1, batch_size = 10, epochs = 300,
                                   callbacks = [callback], shuffle = True, verbose = 0)
        
    def test_model(self, _input, _output):
        """Test the model

        Parameters
        ----------
        _input : np.ndarray
            Input values for testing the model
        _output : np.ndarray
            Output values for testing the model

        Returns
        -------
        float
            Tested loss value of the model
        """
        
        evaluation = self.__model.evaluate(x = tf.convert_to_tensor(_input, dtype = tf.float32),
                                           y = tf.convert_to_tensor(_output, dtype = tf.float32),
                                           verbose = 0)
        
        return evaluation