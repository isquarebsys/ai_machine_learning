#http://stamfordresearch.com/titanic-2-logistic-regression/

# Purpose: Predict survial of males boarding in Cherbourg

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 101)

df = pd.read_csv('Titanic_Clean.csv')
# Print the columns in the console
print(df.columns)

# First we need to drop a couple of features
# For logistic regression to work correctly we need to make one Sex and one Embarked variable the ‘reference’ variable
    # For example, if we make male the reference variable then if ‘Female’ is 0 then the model will be for males
    # If female is 1, then the model will show how the change in risk compared to males, if all over variables are equal
    # Here we drop the male variable and if the passenger boarded in Cherbourg
vars_to_drop = ['Sex_male','Embarked_C']
# The prediction is for males boarding in Cherbourg
df = df.drop(vars_to_drop, axis=1)
df

# This is a new column with all the values set to one. The intercept is the predicted outcome if all the other variables are zero
df['_intercept'] = 1

#Here we split the explanatory variable (survived) as y and the independent variables (everything else) as x
    # Therefore we can predict y (survived) based on x (variables)
    # Copy df across and drop Survived
x = df
x = x.drop('Survived', axis=1)

# Set y as the survived column, we need to wrap it in the dataframe to stop it being series
y = pd.DataFrame(df.Survived)

# Make the model
logit = sm.Logit(y, x)

# Fit the model
result = logit.fit()

