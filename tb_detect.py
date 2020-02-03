{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\ri-340\sl259\slmult1\sa160\partightenfactor0

\f0\fs20 \cf0 # Convolutional Neural Network\
# Part 1 - Building the CNN\
# Importing the Keras libraries and packages\
from keras.models import Sequential\
from keras.layers import Conv2D\
from keras.layers import MaxPooling2D\
from keras.layers import Flatten\
from keras.layers import Dense\
\
# Initialising the CNN\
classifier = Sequential()\
\
# Step 1 - Convolution\
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))\
\
# Step 2 - Pooling\
classifier.add(MaxPooling2D(pool_size = (2, 2)))\
\
# Adding a second convolutional layer\
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))\
classifier.add(MaxPooling2D(pool_size = (2, 2)))\
\
# Step 3 - Flattening\
classifier.add(Flatten())\
\
# Step 4 - Full connection\
classifier.add(Dense(units = 128, activation = 'relu'))\
classifier.add(Dense(units = 1, activation = 'sigmoid'))\
\
# Compiling the CNN\
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])\
\
# Part 2 - Fitting the CNN to the images\
from keras.preprocessing.image import ImageDataGenerator\
\
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)\
test_datagen = ImageDataGenerator(rescale = 1./255)\
training_set = train_datagen.flow_from_directory('dataset/training_set',target_size = (64, 64), batch_size = 32, class_mode = 'binary')\
\
test_set = test_datagen.flow_from_directory('dataset/test_set', target_size = (64, 64), batch_size = 32, class_mode = 'binary')\
classifier.fit_generator(training_set, _per_epoch = 23, = 25, validation_data = test_set, validation_steps = 2)\
\
# Part 3 - Making new predictions\
import numpy as np\
from keras.preprocessing import image\
test_image = image.load_img('dataset/single_prediction/image.png', target_size = (64, 64))\
test_image = image.img_to_array(test_image)\
test_image = np.expand_dims(test_image, axis = 0)\
result = classifier.predict(test_image)\
training_set.class_indices\
if result[0][0] == 0:\
    prediction = 'TB'\
else:\
    prediction = ' NO TB'\
}