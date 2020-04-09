# Solar Potential Estimator 
This dash app allows users to enter the square footage of each face of their roof, along with their home's geographic coordinates, to receive an estimate of the amount of energy that could be produced by adding solar panels to their roof.
## Where do the numbers come from?
A series of Random Forest Regression models were trained on a dataset compiled by Google's Project Sunroof. When a user enters information it is plugged into the models, and the predictions are then returned to the page to display estimates.
