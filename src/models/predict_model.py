from sklearn.linear_model import LinearRegression
from src.features.build_features import prep_data
import matplotlib.pyplot as plt

import pickle
import json

def evaluate():
  model_file = "models" + "/" + "bike_model.h5"
  scores_file = "reports" + "/" + "score.json"
  graph_file = "reports/figures" + "/" + "prediction.png"


  xtrain, ytrain,xtest, ytest = prep_data()

  loaded_model = pickle.load(open(model_file, 'rb'))

  y_pred = loaded_model.predict(xtest)


  # Plotting Scatter graph to show the prediction
  # results - 'ytrue' value vs 'y_pred' value
  plt.scatter(ytest, y_pred, c = 'green')
  plt.xlabel("Bike Counts")
  plt.ylabel("Predicted value")
  plt.title("True value vs predicted value : Linear Regression")
  plt.savefig(graph_file)


  from sklearn.metrics import mean_squared_error, mean_absolute_error
  from sklearn.metrics import r2_score
  mse = mean_squared_error(ytest, y_pred)
  mae = mean_absolute_error(ytest,y_pred)
  R2 = r2_score(ytest,y_pred, multioutput='variance_weighted')
  print("Mean Square Error : ", mse)
  print("Mean Absolute Error : ", mae)
  print("R2 : ",R2)
  
  with open(scores_file, "w+") as f:
    scores = {
      "MSE": mse,
      "MAE": mae,
      "R2" : R2
    }
    json.dump(scores, f, indent=4)
 
if __name__=="__main__":
    evaluate()
