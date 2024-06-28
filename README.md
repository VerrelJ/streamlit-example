# Google Cloud End-to-End Machine Learning Pipeline Using Chicago Taxi Dataset To Improve Its Service

## Overview:
The goal of this project is to build machine learning to forecast fare by using parameters such as census tract, community area, latitude and longitude and time from the Chicago taxi dataset. The entire process will be explained, from gathering data to assessing the model.
  
## WebApp: 
> Link: https://demo-1-fbhrrojzua-et.a.run.app

![image](https://github.com/VerrelJ/demo-1/assets/135339931/654ce36f-69d7-42cf-9293-64e18a1caa33)
![image](https://github.com/VerrelJ/demo-1/assets/135339931/6cc2cae0-5287-4867-9c80-05f651309e79) 

### Census Tract:
Census code of a city. covered a small area of a city
### Community Area:
Community area code of a city. Covered a big area of a city
### Distance:
Distance used in Meter (m)

## Introduction
In cities like Chicago, where taxi services are vital for transportation, understanding how fares are calculated is essential for both passengers and providers. Various factors, such as distance, time, and traffic, influence taxi costs. The use of machine learning allows for the discovery of deeper insights and the provision of useful suggestions for both passengers and providers. In the end, we hope to improve the efficiency and dependability of taxi services in Chicago and abroad by utilizing Google Cloud's machine learning pipelines to build a scalable framework that can adjust to shifting transportation trends.

## System Architecture
The architecture of the system makes use of machine learning to forecast a Chicago taxi fare. Preprocessing techniques include modifying data types, eliminating superfluous features, and employing queries to handle missing values. The four metrics that are used for training and assessing models are MSE, RMSE, MAE, and MAPE. Model with the best result will be used in the deployment.

## Dataset 
![image](https://github.com/VerrelJ/demo-1/assets/135339931/bd33abce-a73e-4cdb-bd03-7bd511a5205a)


## Model Used
SVM (Support Vector Machine),
CatBoost,
Linear Regression,
Random Forest,
XGBoost (Extreme Gradient Boosting)

## Evaluation and Analysis 
CatBoost model produced the greatest results With an MSE of 10.5922, RMSE of 3.2546, MAE of 1.3363, and MAPE of 0.1462 making the best model for deployment

## Conclusion
The research uses information from the Chicago taxi dataset and machine learning to forecast fare. CatBoost outperformed other models that will be used, achieving the best results and used in the deployment to forecast taxi fare in the deployment environment.
