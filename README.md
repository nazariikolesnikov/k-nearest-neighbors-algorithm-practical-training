# Analytical Report: Predictive Classification of Wine Preferences Based on Chemical Properties

### Technologies 

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

The dataset (wine_collection.csv) contains 1,000 records. Each record describes the chemical profile of a wine based on 13 numerical characteristics: alcohol content, malic acid concentration, ash content, ash alkalinity, magnesium, concentration of total phenols, flavonoids, non-flavonoid phenols, proanthocyanidins, color, intensity, hue, OD280 and OD315 in diluted wines, proline, and wine category. 

The target variable is “Desired,” which serves as a marker for the wine class and has three unique values (0, 1, and 2). The classes are distributed almost evenly (0 – 33.8%, 2 – 33.3%, 1 – 32.9%), which is an excellent indicator for building predictive analytics, since we do not need to apply additional sample balancing methods (such as SMOTE) and the model will not be biased toward the majority class.

## Data Preprocessing

To prepare the data for training the neural network, several important steps for cleaning and transforming the data were performed:
The columns “Color,” “Desires,” and “No.” were removed from the dataframe. Removing these columns is necessary to avoid data type errors, although they could be converted to numeric values in the future.

The data was successfully split into a feature matrix (X) and a target variable vector (y). The split into training and test sets was performed in the classic 67/33 ratio with a fixed `random_state = 12345`, which ensures the reproducibility of the experiment.
One-Hot Encoding (to_categorical) was used, which converted the one-dimensional array of the target variable into a three-column matrix to enable multi-class classification.

## Neural Network Architecture

A sequential feedforward neural network was constructed, consisting of the following layers:
An input layer that accepts a vector of 13 features. Hidden layers, consisting of two dense layers with 9 and 10 neurons, respectively, using the ReLU activation function, which is well-suited for addressing the vanishing gradient problem.

An output layer consisting of 3 neurons with a Softmax activation function, which converts the output signals into probabilities of belonging to each of the three wine classes. For training, we selected one of the most effective adaptive gradient descent algorithms—the Adam optimizer—and the categorical_crossentropy loss function.

## Analysis of the Training Process and Growth Points

Analyzing the training logs (up to epoch 110), a certain stagnation can be observed: accuracy fluctuates between 30% and 39%, and the loss function has plateaued at ~1.1–1.3. In fact, at this stage, the model is performing at the level of random guessing, where the probability of guessing correctly by chance for the three classes is 33.3%.

## Main Cause and Recommendation

There is a huge range of scales in the data; for example, the Proline metric reaches values over 1,400, while Nonflavanoid Phenols is around 0.3. It is extremely difficult for neural networks to optimize their weights when the input data varies by several orders of magnitude. As we usually do to improve model stability, before passing the X_train and X_test matrices to the model, it is worth adding a feature scaling step.

<img width="5647" height="3107" alt="Time Series Forcasting (ARIMA)" src="https://github.com/nazariikolesnikov/k-nearest-neighbors-algorithm-practical-training/blob/main/Error%20rate%20for%20different%20values%20of%20K.png" />


