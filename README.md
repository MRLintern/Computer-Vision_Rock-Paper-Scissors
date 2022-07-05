# Computer-Vision_Rock-Paper-Scissors

NOTE: This work is in progress; ML hasn't been incorporated yet.

Play Rock Paper Scissors against the CPU with OpenCV and Machine Learning.

# Requirements and Dependencies
Operating System:`Ubuntu 20.04`, running `Python 3.8`.

The following libraries/frameworks are required:

1. `OpenCV`
2. `TensorFlow`
3. `Keres`

`OpenCV` is a library of programming functions mainly aimed at real-time computer vision.
`TensorFlow` is a library focused on training and inference of deep neural networks.
`Keres` is the API for `TensorFlow`.

# Teachable Machine
This application makes use of [Teachable Machine](https://teachablemachine.withgoogle.com/), an easy way to make machine learning models.
There are three required steps:

1. Gather and group your data into classes or categories, that you want the computer to learn. These are images or audio signals.
2. Train your model, then instantly test it out to see whether it can correctly classify new examples.
3. Download the model. This will be a `.h5` file which will need extracting.


# Model Verification Check
Once you have `"YOUR-MODEL.h5"`,`modelRunCheck.py` can be used to verify that the model loads sucessfully. 

`$ python3 modelRunCheck.py`

# Classic Rock Paper Scissors Base Code
Run `RPS_Classic.py` to play against the computer.
This is the "classic" version of the game. 

`$ python3 RPS_Classic.py`

