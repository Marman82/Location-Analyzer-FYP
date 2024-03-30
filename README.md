# How to train model

Open file in [GitHub Pages](https://github.com/Marman82/Location-Analyzer-FYP/blob/main/analyzer/CNN.py) then execute the code

Default Requirement:

1. Trainning Image inside `analyzer/TrainningSet/my_train`
2. Testing Image inside `analyzer/TrainningSet/my_test`

# Run Frontend

Code for running `React Project` in `/map`

```
npm run start
```

Steps:

1. Click upload button
2. Select the image to predict (Limit to predict location stored in `analyzer/longlat.xlsx`)
3. Wait for the prediction to run, the result will be automatically shown in the map

# Run Backend

Code for running `fastapi` in `analyzer/main.py`

```
uvicorn main:app --reload
```
