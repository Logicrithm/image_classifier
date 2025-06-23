import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

class_names=[ "airplane","automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

model=None

def load_model_and_predict(img):
    global model
    if model is None:
        model=load_model("cifar10_cnn_model.h5")
        
    img = img_to_array(img)/255.0
    img = np.expand_dims(img, axis=0)
    
    pred= model.predict(img)[0]
    class_index=np.argmax(pred)
    confidence= pred[class_index]*100
    
    return class_names[class_index], confidence        
