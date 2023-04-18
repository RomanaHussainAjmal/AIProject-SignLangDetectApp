from flask import Flask,render_template,Response,  send_from_directory
import os
import tensorflow as tf
import cv2
import mediapipe as medpipe
import numpy as np
import time
import pandas as pd
import sys
sys.path.insert(0, 'opencv')



from opencv.cv2AndPrediction import cv2AndPrediction

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    Response(cv2AndPrediction(),mimetype='multipart/x-mixed-replace; boundary=frame')
    return render_template('index.html')

@app.route('/audio/<filename>')
def PredictedTxtAudio_func(filename):
    return send_from_directory(os.path.join(os.getcwd(),'media'),filename)

@app.context_processor
def inject_timestamp():
    return {'timestamp': int(time.time())}


if __name__ == "__main__":
    app.run(debug=True)