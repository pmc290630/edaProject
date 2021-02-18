import pandas as pd
from scipy import stats
import numpy as np


df0 = pd.read_csv("kc_house_prices/King_County_House_prices_dataset.csv")
for c in df0.columns: df0.rename(columns={c:c.replace(" ","-").lower()})
df0["sqft_basement"] = df0["sqft_basement"].transform(lambda x: float(str(x).replace('?',"0.0")))

df_reg = df0.copy()
drop_cols = ["id", "waterfront", "lat", "long", "yr_renovated"]
num_cols = ["sqft_living","sqft_lot","sqft_above","sqft_basement","yr_built","sqft_living15","sqft_lot15"]
cats_cols = ["date","bedrooms","bathrooms","floors","view","condition","grade","zipcode"]

df_reg.drop(drop_cols, axis = 1, inplace= True)
df_reg.dropna(inplace= True)
df_reg["date"] = df_reg["date"].transform(lambda x: pd.to_datetime(x).month)

s = ""
for c in num_cols: s += c + "+"
for c in cats_cols: s += "C({:})+".format(c)
s=s[:-1]




import statsmodels.formula.api as smf
model = smf.ols(formula="price~"+s, data=df_reg).fit()



import pickle
filename = 'KingCountyRegressionModel.sav'
pickle.dump(model, open(filename, 'wb'))
