from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

X=np.array([[1],[2],[3],[4],[5]])
y=np.array([30000,40000,50000,60000,70000])

model=LinearRegression()

model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))