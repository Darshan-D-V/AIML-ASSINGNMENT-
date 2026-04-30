import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

#datasets
data={
    "Area":[1000,1500,2000,2500,3000],
    "Bedrooms":[2,3,3,4,4],
    "Price":[50,70,80,100,120]
}

df=pd.DataFrame(data)

X=df[["Area","Bedrooms"]]
y=df["Price"]

model=LinearRegression()

model.fit(X,y)

#predition
new_house=pd.DataFrame([[2200,3]], columns=["Area","Bedrooms"])


predicted_price=model.predict(new_house)
print("Predicted Price:",predicted_price[0])
