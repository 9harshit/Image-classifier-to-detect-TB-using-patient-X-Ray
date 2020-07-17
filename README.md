# TB Detect: 
* Convolution Neural Network is used to detect TB in patients using X-ray. The user needs to upload their chest X-ray and the system gives them probability of them having TB.
* The system was trained and tested on two publicly available datasets: Sbenzhen chest X-ray set and Montgomery Country chest X-ray set (MC). Accuracy of 85 percent was achieved.
* The patient can use this web application as a second opinion to confirm diagnosis.


## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, matplotlib, sklearn, tensorflow , flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  

## Data Set
Dataset is downloaded from kaggle.com
The data in in data.csv. The number of columns is 30 and the number of rows is 570. The columns are:
For more detail info please visit :https://lhncbc.nlm.nih.gov/publication/pub9931

## Model Building 

First, I have scaled the data with MinMaxScaler. I also split the data into train and tests sets with a test size of 20%.   

I have applied Convolution Neural Network (CNN) with two Convolution layers:
 
*	**Output Layer** – Units=1, activation=binary crossentropy

I have also applied early stopping.

## Model performance 
*	**Validation loss** : 0.0115
*	**Validation Accuracy** : 0.85 or 85%

## Productionization 
In this step, I built a flask API endpoint that is hosted on Heroku. The API endpoint takes in a request with a X-Ray scan of lungs and returns whether the TB is detected or not.

**Application link:** https://tb-detector.herokuapp.com/

![alt text](https://github.com/9harshit/Image-classifier-to-detect-TB-using-patient-X-Ray/blob/master/README_IMG/form.png "TB Detect Form")

![alt text](https://github.com/9harshit/Image-classifier-to-detect-TB-using-patient-X-Ray/blob/master/README_IMG/prediction.png "Result")
