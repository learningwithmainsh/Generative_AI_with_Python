# Purspose - Create Data Model for Machine Learning
from sklearn.linear_model import LinearRegression
import pickle

#Example dataset
houseDataset = [[1000,2],[2200,3],[4000,4],[6000,5]] # Features: [Areas, Rooms]
price = [200000,370000,600000,85000] # Target: Price

model = LinearRegression()
model.fit(houseDataset,price)

with open("house_price_model.pkl","wb") as file:
    pickle.dump(model,file)
