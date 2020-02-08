#Simple python program to implement hyperparamaters optimisation / tuning

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

#It contains model features that require fine tuning
hyp_params= { 
    'n_estimators': [300, 700],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth':np.arange(5,15,1)
}

#Grid Search
grid_ram = GridSearchCV(estimator=rf, param_grid=hyp_params, cv= 5)
grid_ram.fit(X, y)
print(grid_ram.best_params_)


#Random Search
grid_ram= RandomizedSearchCV(estimator=rf, param_distributions=hyp_params, cv= 5,n_iter=100)
grid_ram.fit(X, y)
print(grid_ram.best_params_)

#SMBO yet to implement and will be added 
