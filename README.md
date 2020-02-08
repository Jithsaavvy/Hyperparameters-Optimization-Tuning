# Hyperparameters-Optimization-Tuning

Developed a python code using sklearn that implements the concept of hyperparameters and algorithms for hyperparameters optimization/tuning.

Hyperparameters are a model’s inbuilt configuration variables. These variables require fine tuning to produce a better performing model. These parameters are model dependent and vary from model to model.

Grid Search is the most basic algorithmic method for hyper-parameter optimization . It is similar to running nested loops on all possible values of the inbuilt features. The hyp_params in the code below contains model features that require fine tuning.

Random Search is grid search where the next feature set is selected randomly and the total number of runs have a upper limit. Code for random search is same as GridSearch only difference is that n_iter=100 is added which fixes an upper limit on the number of allowed runs. Grid/Random search are examples of uninformed search that means next of feature set is independent of the output of the last runs. Both of them require retraining in every iteration which incurs a huge cost.

Sequential Model Based Optimisation (SMBO) minimises validation loss by sequentially selecting different hyperparameter sets where next set is selected by bayesian reasoning (depending on the previous runs). Intuitively speaking SMBO looks back at the result of last runs to focus future searches on areas which look more promising. I will implement the code for SMBO in forthcoming days.

Reference: https://towardsdatascience.com
