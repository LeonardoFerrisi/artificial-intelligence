from keras.datasets import mnist
from matplotlib import pyplot
import numpy as np
import time

class Encoder:

    def __init__(self):
        (train_X, train_y), (test_X, test_y) = mnist.load_data()

        self.train_X = train_X.astype('float32')
        self.train_y = train_y
        self.test_X = test_X.astype('float32')
        self.test_y = test_y
        
        # NORMALIZE
        self.train_X /= 255
        self.test_X /= 255
        
    def splitup(self, arr, nrows, ncols):
        """
        Return an array of shape (n, nrows, ncols) where
        n * nrows * ncols = arr.size

        If arr is a 2D array, the returned array should look like n subblocks with
        each subblock preserving the "physical" layout of arr.
        """
        h, w = arr.shape
        assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
        assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
        return (arr.reshape(h//nrows, nrows, -1, ncols)
                .swapaxes(1,2)
                .reshape(-1, nrows, ncols))
                
    def encodeAll(self, subDimension=7):
        self.encodedXtrain = []
        self.encodedYtrain = []

        for i in range(len(self.train_X)):
            encodedX = self.encode(self.train_X[i], subDimension)
            self.encodedXtrain.append(encodedX)
            self.encodedYtrain.append(self.getYencode(self.train_y[i]))

    def plot(self, num=9):
        for i in range(num):  
            pyplot.subplot(330 + 1 + i)
            pyplot.imshow(self.train_X[i], cmap=pyplot.get_cmap('gray'))
        pyplot.show()

    def encode(self, data, subDimension=7):
        fracture = self.splitup(data, subDimension, subDimension)
        encoded = []
        for i in range(len(fracture)):
            encoded.append(np.mean(fracture[i]))
        return encoded
    
    def getYencode(self, number):
        zero = [0] * 10
        if number == 0: 
            return zero
        else:
            zero[number-1] = 1
            output = zero
            return output



if __name__ == "__main__":

    e = Encoder()

    # for i in range(9):
    #     n = e.encode(e.train_X[i])
    #     n1 = e.getYencode(e.train_y[i])
    #     print(n)
    #     print(n1)
    #     print("\n")

    # e.plot()

    t1 = time.time()
    # n = e.encode(e.train_X[0], subDimension=4)
    
    # print(np.shape(n))
    e.encodeAll(subDimension=4)

    t2 = time.time()

    timeElapsed = t2 - t1
    print(f"Time elapsed: {timeElapsed}")
    print(len(e.encodedXtrain[0]))
    print(len(e.encodedYtrain[0]))
    print(e.encodedXtrain[0])
    print(e.encodedYtrain[0])