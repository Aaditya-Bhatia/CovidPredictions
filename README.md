# CovidPredictions
Predictions for the nation with the fastest-growing Covid-19 cases.

The top three countries with the maximum number of COVID cases are the USA, Brazil, and India. Currently, the USA holds the crown for max cases in the world. However, this "crown is in rotation" [https://www.youtube.com/watch?v=rAAdQQhEc2I]. 

The question is-when? 

I used Machine Learning approaches to analyze and predict time series data. I used Facebook's library, fbprophet to generate an adaptive forecasting model. This works great on non-linear trends & takes the seasonality-effect and holiday-effect into account.

Prediction results:
**The number of cases in India will surpass the number of cases in Brazil on *Sep14th*.**
These predictions are very close to the actual date(Sep7th). Predictions were off by one week only.

The same model predicts that the **Cases in India will surpass cases in the USA on *Apr9th, 2021*.** 
The model's predictions are based on the *past* rate of spread per country, and cannot predict if covidiots spread more cases during the holiday season 😠 !

## Prediction
![](https://github.com/Aaditya-Bhatia/CovidPredictions/blob/master/Covid_predictions.png)

## Current trend
![](https://github.com/Aaditya-Bhatia/CovidPredictions/blob/master/Covid_actual.png)
