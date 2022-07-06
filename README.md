SeoulBikePrediction
==============================

Mlops pset 2
------------

Description
------------

Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern.
The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes. The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour, and date information. This project predicts the number of rental bike count for seoul city.

Dataset source
------------
https://www.kaggle.com/c/seoul-bike-rental-prediction

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.(has SeoulBikeData.csv)
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries (has our model saved)
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. (metrics are stored here)
    │   └── figures        <- Generated graphics and figures to be used in reporting (has the prediction figure)
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt` (contains requirements for the project)
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py  (transforms data for trains, extracts month, day from date)
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py  (prediction & evaluation)
    │   │   └── train_model.py   (model training)
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
    
    
    dvc.yaml file has the dvc pipeline.
    app.py Entry point for web app deployment code.
 
 *Have written in (), what each file contains for the project.
 
DVC Pipeline 
------------
 The DVC pipeline has 3 stages for preparing the data, training the model and evaluating it.
 ![azure_sample](https://user-images.githubusercontent.com/6350912/177523625-436b71b5-4619-457f-b7e2-29a18110c83c.PNG)

CML
------------
 CML Github action workflow is created and it is triggered on every push.
 It creates a docker instances, install dependencies and execute the dvc stages.
 The report of the execution is kept in reports folder.
 ![prediction](https://user-images.githubusercontent.com/6350912/177524415-6a4afc2b-4c36-4a8a-9ffa-6f877e758bf5.png)
 
Cloud Deployment(Azure)
------------
 Have linked the project to Azure.
 It can be easily deployed using Azure web service api.
 ![azure_screen](https://user-images.githubusercontent.com/6350912/177524440-87029adc-a579-47ca-9ecd-678320e82cb7.PNG)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
