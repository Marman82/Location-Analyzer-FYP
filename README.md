# How to train model

Open file in [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/CNN.py) then execute the code

Default Requirement:

1. Trainning Image inside [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/tree/main/analyzer/TrainningSet/my_train/my_train)
2. Testing Image inside [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/tree/main/analyzer/TrainningSet/my_test/my_test)

# Run Frontend

Code for running `React Project` in [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/tree/main/map)

```
npm run start
```

Steps:

1. Click upload button
2. Select the image to predict (Limit to predict location stored in [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/longlat.xlsx))
3. Wait for the prediction to run, the result will be automatically shown in the map

# Run Backend

Code for running `fastapi` in [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/main.py)

```
uvicorn main:app --reload
```
