# Analytical Report: Predictive Classification of Wine Preferences Based on Chemical Properties

### Technologies 

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Executive Summary

The purpose of this analysis is to examine the chemical characteristics of various wine samples and develop a machine learning classification model to predict whether a wine meets the "Desired" criteria. Data from 178 wine samples were processed and analyzed. The analytical pipeline integrates comprehensive data preprocessing, feature scaling, and the deployment of a K-Nearest Neighbors (KNN) classification algorithm to assess the dataset and identify predictive patterns.

## Data Structure and Key Statistical Indicators

The study identified the following key parameters and structural indicators within the dataset:

* The dataset contains a total of 178 instances and 14 initial columns, representing a robust sample of wine observations;
* After excluding non-predictive identifiers (the 'Color' and '№' columns), the dataset was refined to 13 distinct chemical features. These include measurements such as Alcohol, Malic and Apple Acid, Ash, Magnesium, Flavanoids, and Proline;
* The dependent variable is "Desired," a binary indicator where samples are classified as either 1 (desired) or 0 (not desired);
* An initial frequency check of the 'Proline' feature indicates a wide spread of unique values, with the most frequent amounts (1366 and 1357) appearing only 3 times each. This highlights high variance and a continuous distribution among specific chemical markers within the sample. 

<img width="5647" height="3107" alt="Time Series Forcasting (ARIMA)" src="https://github.com/nazariikolesnikov/k-nearest-neighbors-algorithm-practical-training/blob/main/Error%20rate%20for%20different%20values%20of%20K.png" />


