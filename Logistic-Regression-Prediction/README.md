# Prediction using Logistic Regression

In **logistic regression**, the dependent variable is binary or dichotomous, i.e. it only contains data coded as 1 (TRUE, success, pregnant, etc.) or 0 (FALSE, failure, non-pregnant, etc.).

![Logistic Regression](https://user-images.githubusercontent.com/21111859/36820109-4fdc4424-1cba-11e8-92e4-366c4ccf2eca.png)

The goal of logistic regression is to find the best fitting (yet biologically reasonable) model to describe the relationship between the dichotomous characteristic of interest (dependent variable = response or outcome variable) and a set of independent (predictor or explanatory) variables. 

Logistic regression was developed by statistician David Cox in 1958.The binary logistic model is used to estimate the probability of a binary response based on one or more predictor (or independent) variables (features). It allows one to say that the presence of a risk factor increases the odds of a given outcome by a specific factor. The model is a direct probability model and not a classifier.

## Logistic Regression Assumptions:

   - Binary logistic regression requires the dependent variable to be binary.
   - For a binary regression, the factor level 1 of the dependent variable should represent the desired outcome.
   - Only the meaningful variables should be included.
   - The independent variables should be independent of each other. That is, the model should have little or no       
      multicollinearity.
   - The independent variables are linearly related to the log odds.
   - Logistic regression requires quite large sample sizes.


Logistic regression generates the coefficients (and its standard errors and significance levels) of a formula to predict a logit transformation of the probability of presence of the characteristic of interest:

_Logistic regression equation_

where p is the probability of presence of the characteristic of interest. The logit transformation is defined as the logged odds:

**Odds=p/(1-p)**

and

**Logit(p)=ln(p/(1-p))**

Rather than choosing parameters that minimize the sum of squared errors (like in ordinary regression), estimation in logistic regression chooses parameters that maximize the likelihood of observing the sample values. The logit of success is then fitted to the predictors. The predicted value of the logit is converted back into predicted odds via the inverse of the natural logarithm, namely the exponential function. Thus, although the observed dependent variable in binary logistic regression is a zero-or-one variable, the logistic regression estimates the odds, as a continuous variable, that the dependent variable is a success (a case). In some applications the odds are all that is needed. In others, a specific yes-or-no prediction is needed for whether the dependent variable is or is not a case; this categorical prediction can be based on the computed odds of a success, with predicted odds above some chosen cutoff value being translated into a prediction of a success.

The assumption of linear predictor effects can easily be relaxed using techniques such as spline functions.


**References:** 
1) ![MedCalc](https://www.medcalc.org/manual/logistic_regression.php)
2) ![Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)
