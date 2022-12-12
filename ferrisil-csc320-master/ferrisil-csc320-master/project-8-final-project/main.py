from network import Network
from encoder import Encoder
import time

if __name__ == "__main__":
    
    e = Encoder()
    
                                # data starts at 28 x 28, scaled down in divisible numbers like 7, 4, 2
    e.encodeAll(subDimension=4) # use if you want 7 x 7 dataset for total of 49 inputs
    # e.encodeAll(subDimension=7) # use if you want 4 x 4 dataset for total of 16 possible inputs

    
    # n = e.encodedXtrain[0]
    
    # print(np.shape(n))
    
    a = Network(49, 28, 28, 10, learningRate=0.6, tolerance=0.1)
    # a = Network(16, 7, 10, 10, learningRate=0.4, tolerance=0.2)
    
    inputs = e.encodedXtrain[:60]
    targets = e.encodedYtrain[:60]

    a.setInputs(inputs)
    a.setTargets(targets)
    a.test(VERBOSE=False)
    time.sleep(2)
    t1 = time.time()
    a.train(cycles=100000, sleeptime=0.003)
    t2 = time.time()
    timeElapsed = t2 - t1
    print(f"Time Elapsed: {round(timeElapsed,2)}")
    a.test(VERBOSE=False)