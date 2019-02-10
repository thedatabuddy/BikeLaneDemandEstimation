from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import r2_score


inpfile=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\normalized_scores.csv')

x_inp=inpfile[['accident_count','business_count']]
y_inp=inpfile['norm_score']

x_train, x_test, y_train, y_test = train_test_split(x_inp, y_inp, test_size=0.4,random_state=0)

lr=LinearRegression()

lr.fit(x_train,y_train)

y_train_pred = lr.predict(x_train)
y_test_pred = lr.predict(x_test)

train_accuracy = r2_score(y_train, y_train_pred)
test_accuracy = r2_score(y_test, y_test_pred)
print('The training accuracy is', train_accuracy*100)
print('The test accuracy is', test_accuracy*100)
print('Coefficients',lr.coef_)
print('Intercept',lr.intercept_)

### Plotly code

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
x =inpfile['accident_count'].values
y =inpfile['business_count'].values
z =inpfile['norm_score'].values

x_surf, y_surf = np.meshgrid(np.linspace(x.min(), x.max(), 100),np.linspace(y.min(), y.max(), 100))
onlyX = pd.DataFrame({'accident_count': x_surf.ravel(), 'business_count': y_surf.ravel()})
fittedY=lr.predict(onlyX)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='blue', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='None', alpha=0.1)

ax.set_xlabel('accident_count')
ax.set_ylabel('business_count')
ax.set_zlabel('norm_score')
plt.show()