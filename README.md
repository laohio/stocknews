Author: Nicholas A. Ficeto <br>
Date: 2018/08/02

OVERVIEW
--------
The purpose of this app is to demonstrate the myriad ways that real-world events can affect stock prices.  To achieve this, 
I've created a user interface that combines a stock chart displaying closing prices over a 100-day span along with news articles corresponding to certain dates, like the day of the biggest drop in the stock's price -- currently this is the only "special date" I have implemented.

EXAMPLE 1:
<img width="1280" alt="screen shot 2018-08-02 at 9 57 49 pm" src="https://user-images.githubusercontent.com/16903793/43620136-3e90efe4-969f-11e8-83b2-17979bb55d63.png">

<img width="1279" alt="screen shot 2018-08-02 at 9 46 54 pm" src="https://user-images.githubusercontent.com/16903793/43619952-58b4a18c-969e-11e8-81aa-1688d83a8f62.png">

EXAMPLE 2:
<img width="1278" alt="screen shot 2018-08-02 at 10 00 46 pm" src="https://user-images.githubusercontent.com/16903793/43620227-a93165fe-969f-11e8-9f86-e7d8c6b97b74.png">

<img width="1280" alt="screen shot 2018-08-02 at 10 01 03 pm" src="https://user-images.githubusercontent.com/16903793/43620232-b22cb262-969f-11e8-9eab-26e0f1559802.png">

The inspiration for this app stems from my personal curiosity to learn more about short-term price fluctuations in the stock
market, and how external forces (e.g. Amazon acquiring Whole Foods) can affect invester confidence.  This is a personal
side project I did for my own learning, and thus may not run perfectly.

IMPLEMENTATION
--------------
I used data from 2 external services to obtain the information I needed to build this app:

1.) Alpha Vantage - A service that provides time series APIs for both real-time and historical stock data.  I use stock data from this service formatted in Pandas-style dataframes to perform any data analysis. <br>
2.) NewsAPI.org - A service that provides JSON data for news articles pertaining to a particular topic. <br>

I also used the scientific graphing libraries provided by "Plotly" to dynamically generate a URL, which is embedded within the HTML to display the stock chart.

Technology Stack: The majority of this program (including application lgoic) was written using Python.

Front-End: Standard HTML/CSS <br>
Back-End: Python Flask Server


I am the sole contributor to this app.
