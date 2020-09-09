#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:45:08 2020
@author: aadityabhatia

Info: covid predictions uses Facebook time series prediction library, fbprophet
to predict future cases. 
The main goal is to find when India will have max cases in the world.
"""

from fbprophet import Prophet
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/aadityabhatia/Downloads/Covid-19_visualizations_Page 1_Combo chart.csv')
df['date'] = pd.to_datetime(df.date)

us = df[df.Country == 'United_States_of_America']
ind = df[df.Country == 'India']
bra = df[df.Country == 'Brazil']

#%%

us = us.rename(columns={'date': 'ds', 'confirmed_cases': 'y'})

us_model = Prophet(interval_width=0.95)
us_model.fit(us)

us_forecast = us_model.make_future_dataframe(periods=240, freq='D')
us_forecast = us_model.predict(us_forecast)

fu = us_forecast.copy()

us_model.plot(us_forecast)

us_cols = ['us_{}'.format(col) for col in us_forecast.columns]
us_forecast.columns = us_cols


#%%
bra = bra.rename(columns={'date': 'ds', 'confirmed_cases': 'y'})

bra_model = Prophet(interval_width=0.95)
bra_model.fit(bra)

bra_forecast = bra_model.make_future_dataframe(periods=240, freq='D')
bra_forecast = bra_model.predict(bra_forecast)

fb = bra_forecast.copy()

bra_cols = ['bra_{}'.format(col) for col in bra_forecast.columns]
bra_forecast.columns = bra_cols

#%%

ind = ind.rename(columns={'date': 'ds', 'confirmed_cases': 'y'})

ind_model = Prophet(interval_width=0.95)
ind_model.fit(ind)

ind_forecast = ind_model.make_future_dataframe(periods=240, freq='D')
ind_forecast = ind_model.predict(ind_forecast)

fi = ind_forecast.copy()

ind_cols = ['ind_{}'.format(col) for col in ind_forecast.columns]
ind_forecast.columns = ind_cols

#%% new plotting all 3 in one
fig = plt.figure()
a1 = fig.add_subplot()
us_model.plot(fu)

a2 = fig.add_subplot()
ind_model.plot(fi)
#%% merging the df

ind_bra = pd.merge(ind_forecast, bra_forecast, how = 'inner', left_on = 'ind_ds', right_on = 'bra_ds')
ind_bra_us = pd.merge(ind_bra, us_forecast, how = 'inner', left_on = 'ind_ds', right_on = 'us_ds')

forecast = ind_bra_us.copy()
forecast['Date'] = forecast['ind_ds']


#%% date when india surpasses usa cases and brazil cases
f = forecast[['ind_yhat', 'bra_yhat', 'us_yhat', 'Date']]
f = f[f['Date'] > dt.datetime(2020,8,2)]
f[f.ind_yhat > f.bra_yhat].Date.min()
f[f.ind_yhat > f.us_yhat].Date.min()

#%% Plotting

plt.rcParams.update({'font.size':12})
plt.plot(forecast['Date'], forecast['ind_yhat'], 'b-', label = 'India')
plt.plot(forecast['Date'], forecast['us_yhat'], 'r-', label = 'USA')
plt.plot(forecast['Date'], forecast['bra_yhat'], 'g-', label = 'Brazil')

plt.legend(); plt.xlabel('Date', fontsize='13'); plt.ylabel('Cases (in 10 million)', fontsize='13')
plt.xticks(rotation='90', fontweight='bold');plt.yticks(fontweight='bold')

plt.axvline(dt.datetime(2021,4,9), ls = ':')
plt.axvline(dt.datetime(2020,9,14), ls = ':')
plt.title('Predicted Cases')
plt.savefig('Covid_predictions.png', bbox_inches='tight')

#%% currnet trend

plt.rcParams.update({'font.size':12})
plt.plot(ind['ds'], ind['y'], 'b-', label = 'India')
plt.plot(us['ds'], us['y'], 'r-', label = 'USA')
plt.plot(bra['ds'], bra['y'], 'g-', label = 'Brazil')

plt.legend(); plt.xlabel('Date', fontsize='13'); plt.ylabel('Cases (in 10 million)', fontsize='13')
plt.xticks(rotation='90', fontweight='bold');plt.yticks(fontweight='bold')
plt.ylim(0,20000000)
#plt.xlim(forecast.Date.min(),forecast.Date.max())
plt.title('Actual Cases')
plt.savefig('Covid_actual.png', bbox_inches='tight')