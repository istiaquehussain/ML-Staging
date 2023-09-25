---ML Staging--- 

This project aims to explain various steps envolve in a typical ML projects starting from development till deployment 


- Table of Contents

/presentation ->  contains all presentation files

/core -> contains all source codes

- Source codes 

Real_estate.csv - data source for the the real state model training 

RealState_Model_Src.py - Source code for model selection, training and generation 

RealState_API_Scr.py - Source code for model integration with web framework 

RealState_Home.html -  sample Front End page to access Model API

GPT_Prompt.txt - Chat GPT Prompt to generate RealState_Home.html Contents

-Steps 
1. Install python from https://www.python.org/downloads/
2. Install all required python modules
    pip install numpy
    pip install pandas
    pip install scikit-learn
    pip install flask-ngrok
    pip install pyngrok
    pip install flask_cors
    
3. clone the repository 
4. go to /core folder 
5. edit RealState_Model_Src.py file to modify the path for the location of 
    a. Real_estate.csv
    b. model.pkl 
6.  edit RealState_API_Scr.py file to modify the path for the location of 
    a. model.pkl 
       
6. for model selection, training and generation run RealState_Model_Src.py as 
  python3 RealState_Model_Src.py
7. To host the model as API (Service) run RealState_API_Scr.py as
  python3 RealState_API_Scr.py
8. test the model api as
   a. curl -d '{ "age": 15, "distance": 500, "nos": 10 }' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predict
   b. open RealState_Home.html in chrome browser 
   
-----Enjoy------   
        


