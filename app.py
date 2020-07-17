from flask import Flask, redirect, url_for, render_template, request, session
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/", methods = ["POST", "GET"])  # this sets the route to this page
def home():
    if request.method == "POST":
        if request.files:
            image =  request.files["image"]
            model = load_model('cnn.h5')
            test_image = image.load_img(image, target_size = (64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = model.predict(test_image)

            if result[0][0] == 1:
                session["result"] = 1
            else:
                session["result"] = 0

            return render_template("home.html", result = session["result"])

        else:
            print("File not found")
            return render_template("home.html", result = 2)

        
    else:
        return render_template("home.html", result = 2)



if __name__ == "__main__":
    app.run(debug = True)
