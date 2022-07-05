import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np

def prepareData(data, max_days=None):
  X = data.drop(['Rented Bike Count'], axis=1)
  y = data['Rented Bike Count']
  X['Seasons'].replace(['Summer', 'Spring', "Autumn", "Winter"], [0, 1, 2, 3], inplace=True)
  X["Seasons_sin"] = np.sin(2 * np.pi * X['Seasons']/3.0)
  X['Date'] =  pd.to_datetime(X['Date'])
  X["Month"] = np.sin(2 * np.pi * X['Date'].dt.month/12.0)
  if max_days == None:
    max_days = 6.0
  X['Day'] =  np.sin(2 * np.pi * X['Date'].dt.dayofweek/max_days)
  X['Hour_sin'] = np.sin(2 * np.pi * X['Hour']/23.0)
  X['Hour_cos'] = np.cos(2 * np.pi * X['Hour']/23.0)
  X = X.drop(['Date'], axis=1)
  X = X.drop(['Hour'], axis=1)
  X = X.drop(['Seasons'], axis=1)
  return X, y

def prep_data():
  data_file = 'data/raw/SeoulBikeData.csv'
  df = pd.read_csv (data_file, index_col=0,encoding= 'unicode_escape')
  df.reset_index(inplace = True)
  trainDf=df.sample(frac=0.9, random_state=42) #random state is a seed value
  testDf=df.drop(trainDf.index)

  X_train, y_train = prepareData(trainDf)
  X_test, y_test = prepareData(testDf)
  cat_cols = ['Holiday','Functioning Day']
  num_cols = [col for col in list(X_train) if col not in cat_cols]

  num_pipeline = Pipeline([('scaler', StandardScaler())])
  cat_pipeline = Pipeline([('encoder', OneHotEncoder())])
  full_pipeline = ColumnTransformer([('num', num_pipeline, num_cols),('cat', cat_pipeline, cat_cols)])

  #Data preparation
  X_train_prepared = full_pipeline.fit_transform(X_train)
  X_test_prepared = full_pipeline.transform(X_test)
  return X_train_prepared,y_train,X_test_prepared,y_test

if __name__=="__main__":
  x_train,y_train,x_test,y_test = prep_data()
