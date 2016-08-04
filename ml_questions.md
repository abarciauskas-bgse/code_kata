[questions from glassdoor](https://www.glassdoor.com/Interview/Amazon-com-Machine-Learning-Scientist-Interview-Questions-EI_IE6036.0,10_KO11,37.htm)
[questions on quora](https://www.quora.com/How-should-I-prepare-for-an-interview-with-the-Amazon-machine-learning-group)

## Bootstrapping


## Confidence Intervals and their significance

[resource](http://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading24.pdf)

Bootstrapping (sampling with replacement) approximates the variation in a statistic (e.g. the mean). If the empirical mean is x, then a confidence interval for the true mean can be estimated using a boostrapping technique. Create say 20 samples of 100 random draws each from the data. Compute the empirical mean of each sample and subtract it from the mean of the observed data. Thus we have 20 deviations from the empirical mean. We order these 20 deviations and to get an 80% confidence interval we can take the 18th and 2nd items, add and subtract them from the empirical mean to arrive at the confidence interval.

## Law of Large Numbers

With enough data, the empirical distribution is a good estimation of the true distribution.

## how over sampling works

One can oversample the under-represented (minority) class or do synthetic oversampling.


## significance of the ROC curve and how to interpret a ROC curve

When the cost function is different for different classes it makes sense

## How Random forest works
## Practical experience about Overfitting and Underfitting

## Practical experience about variable selection

## Basics of Logistic Regression

## What's the difference between MLE and MAP inference?

MLE is the estimate for a hyperparameter which maximizes the probability of the data given the hyperparameter. It is prone to overfit the training data. MAP puts a prior on the hyperparameter so the optimal parapmeters is the parameter which maximizes the joint probability of the data given the parameter times the probability of the data. These can be computed:

* analytically if the mode of the posterior distribution are available in closed form via conjugate priors. 
* via numerical optimization, e.g. gradient descent
* via the EM algorithm
* via Monte Carlo method or simulated annealing

## What is the EM algorithm

## what is monte carlo method?

## How to deal with unbalanced data where the ratio of positive and negative is huge.

Oversample the minority class or undersample the majority class

## Estimate the disease probability in one city given the probability is very low national wide. Randomly asked 1000 person in this city, with all negative response (NO disease). What is the probability of disease in this city.

## i. Tell me about the supervised machine learning techniques that you know about?

## ii. If you have a customer and want to decide whether they will "buy today" or "not buy today" and you know 1. where they live, 2. their income, 3. their gender, 4. their profession, how would you define a machine learning algorithm.

## iii. How does a neural network with one layer and one input and output compare to a logistic regression.

## What is the curse of dimensionality

[Curse of Dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)

## Why use L1 or L2 regularization?

# Regularization

[Answer from Justin Solomon on Quora](https://www.quora.com/What-is-the-difference-between-L1-and-L2-regularization/answer/Justin-Solomon)

Can be viewed as:

* putting a prior on the distribution from which your data was drawn,
* as a way to punish high values in regression coefficients

*undetermined:* **`Ax = b`** is undertermined when A is wider than it is tall, thus there exists infinitely many solutions. (Multiple possible `x`'s)

Thus we chose to minimize ||x|| wrt Ax = b

## What is boosting?

## Comparing Lasso and Ridge regression

Lasso uses the L1 penalty (sum of absolute values of parameters) where Ridge uses the L2 (sum of squared values of parameters). In regularization you are adding a penalty term to the cost function to reduce the likelihood of overfitting the model to the training data by removing (L1) or shrinking (L2) the parameters.

## Describe SVM. Explain advantages and drawbacks of SVM. 

SVMs are the general form of the optimization problem of mapping an input space into a maximally seperable output space. SVMs may implement a variety of kernel functions mapping the original input space into a different output space. Usually the objective is to map them to a space that is maximally seperable as defined by the optimization problem of minimizes the training error plus the complexity term, or equivalently minimizes the error while simultaneously maximizing the margin.

## Describe linear regression vs. logistic regression.

Linear regression fits parameters to the features which maps into a continuous output space - that is the outputs themselves are a continuous variable. Logistic regression handles the case where the outputs are non-continuous, for example binary classification. Logistic regression handles this by mapping the input feature space into probabilities for each class using the sigmoid function. Parameters for the 

## How to address overfitting?

- Reduce number of parameters, use model selection. The downside is you may lose predictive power, there may actually be explanatory power in those lost parameters

## How would you diagnose bias vs variance problem?

Bias: both high training and test errors
Variance: low training but high test error

