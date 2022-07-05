from sklearn.linear_model import LinearRegression
from src.features.build_features import prep_data

import pickle

def train():
  model_file = "models" + "/" + "bike_model.h5"
  print(model_file)
  
  xtrain,ytrain, xtest, ytest = prep_data()
  regressor = LinearRegression()
  regressor.fit(xtrain, ytrain)

  pickle.dump(regressor, open(model_file, 'wb'))
 
if __name__=="__main__":
    train()
