# This is the MVP.   No end user interaction.   No website
# users submit a json file with the entry and the model
# admin defines a contest with a directory of testing data
#

import json
import argparse
import numpy as np
from glob import glob
from keras.models import load_model
from sklearn.metrics import roc_curve, confusion_matrix

# using model.save you get an h5 model
# using tf.saved_model.save you get a tensorflow checkpoint, which is a directory
# note tf.saved_model changed in version 2.0

parser = argparse.ArgumentParser(description='Evaluate models listed in JSON files')
parser.add_argument('contest_file', help="a json file describing the contest")

args = parser.parse_args()
print(args.contest_file)

xfile = "/Users/gary/Desktop/ML_examples/x_test.npz"
yfile = "/Users/gary/Desktop/ML_examples/y_test.npz"
mfile = "/Users/gary/Desktop/ML_examples/model.10-0.09.h5"
mdir = "/Users/gary/Desktop/ML_examples"

def runModel(mf, xf, yf):
    x_test = np.load(xf)['arr_0']
    y_test = np.load(yf)['arr_0']
    model = load_model(mf)
    print(x_test.shape, y_test.shape)
    print(model.evaluate(x_test, y_test))
    y_hat = model.predict(x_test)
    y_hat_cats = np.argmax(y_hat, axis=1)
    y_test_cats = np.argmax(y_test, axis=1)

    print(confusion_matrix( y_test_cats, y_hat_cats))

mfiles = glob("{}/*h5".format(mdir))
for mfile in mfiles:
    runModel(mfile, xfile, yfile)
 
 
