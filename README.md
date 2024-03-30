# How to train model

Open file in [CNN.py](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/CNN.py) then execute the code

Default Requirement:

1. Trainning Image inside [my_train](https://github.com/Marman82/Location-Analyzer-FYP/tree/main/analyzer/TrainningSet/my_train/my_train)
2. Testing Image inside [my_test](https://github.com/Marman82/Location-Analyzer-FYP/tree/main/analyzer/TrainningSet/my_test/my_test)

# Run Frontend

Code for running `React Project` in [/map](https://github.com/Marman82/Location-Analyzer-FYP/tree/main/map)

```
npm run start
```

Steps:

1. Click upload button
2. Select the image to predict (Limit to predict location stored in [longlat.xlsx](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/longlat.xlsx))
3. Wait for the prediction to run, the result will be automatically shown in the map

# Run Backend

Code for running `fastapi` in [main.py](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/main.py)

```
uvicorn main:app --reload
```

Code for executing prediction [CNNinference.py](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/CNNinference.py)

# Sample Image for Prediction

Fung Yu Ting
![alt text](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/Sample Pred Image/Fung Yu Ting (1).jpg)
Lion Rock
![alt text](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/Sample Pred Image/LION ROCK (2).jpg)
MacLehose Trail M102
![alt text](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/Sample Pred Image/M102 (2).jpg)
MacLehose Trail M103
![alt text](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/Sample Pred Image/M103 (7).jpg)
MacLehose Trail M104
![alt text](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/Sample Pred Image/M104 (4).jpg)
Direction Slab
![alt text](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/Sample Pred Image/Direction Slab (1).jpg)
