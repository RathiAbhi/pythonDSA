import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from sklearn.decomposition import PCA

# Data (with a larger sample size for illustration)
data = {
    'EngineSize': [1.6, 2.0, 2.4, 3.0, 3.5, 2.2, 1.8, 2.6, 2.8, 3.0],
    'Horsepower': [130, 160, 180, 220, 250, 210, 140, 160, 180, 190],
    'Mileage': [30000, 25000, 20000, 15000, 10000, 25000, 22000, 23000, 21000, 24000],
    'Price': [15000, 20000, 25000, 30000, 35000, 28000, 22000, 24000, 26000, 31000]
}
df = pd.DataFrame(data)

# Independent and Dependent Variables
X = df[['EngineSize', 'Horsepower', 'Mileage']]
y = df['Price']

X['random3'] = np.random.rand(len(X))

pca = PCA(n_components=6)
#n_components must be between 0 and min(n_samples, n_features)
x_trans = pd.DataFrame(pca.fit_transform(X))
x_trans.corr()
print(pca.explained_variance_ratio_)

# Check Multicollinearity (VIF)
vif_data = pd.DataFrame()
vif_data['feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("VIF Values:\n", vif_data)

# If VIF is too high, remove the problematic features
# In this case, let's drop 'Horsepower' due to high multicollinearity (VIF)
X = X.drop('Horsepower', axis=1)

# Standardize Predictors
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.4, random_state=42)

# Add a constant to X_train for intercept
X_train_const = sm.add_constant(X_train)

# Fit the OLS model using statsmodels
ols_model = sm.OLS(y_train, X_train_const).fit(cov_type='HC3')

# Print the summary
print(ols_model.summary())

# Predictions
X_test_const = sm.add_constant(X_test)
y_pred = ols_model.predict(X_test_const)

# Evaluate the Model
if len(X_test) > 1:  # Only calculate R^2 if there are more than one test samples
    from sklearn.metrics import mean_squared_error, r2_score
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
    print("R-squared:", r2_score(y_test, y_pred))
else:
    print("Test set too small for R^2 computation.")