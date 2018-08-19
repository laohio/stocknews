Author: Nicholas A. Ficeto <br>
Date: 2018/08/02

OVERVIEW
--------------
The purpose of this app is to create dynamic news dashboards for publicly-traded companies, based on their stock performance.  The inspiration behind this was me wanting to learn more about the myriad ways that real-world events can affect stock prices.  To achieve this, 
I've created a user interface that combines a stock chart displaying closing prices over a 100-day span along with news articles corresponding to certain dates, like the day of the biggest drop in the stock's price -- currently this is the only "special date" I have implemented.

Landing page:
<img width="1280" alt="screen shot 2018-08-03 at 12 13 32 pm" src="https://user-images.githubusercontent.com/16903793/43653891-7c1ddc28-9717-11e8-84c5-5d2297b4f789.png">

EXAMPLE 1 (news articles reflect doubts about driverless technology):
<img width="1280" alt="screen shot 2018-08-02 at 9 57 49 pm" src="https://user-images.githubusercontent.com/16903793/43620136-3e90efe4-969f-11e8-83b2-17979bb55d63.png">

<img width="1279" alt="screen shot 2018-08-02 at 9 46 54 pm" src="https://user-images.githubusercontent.com/16903793/43619952-58b4a18c-969e-11e8-81aa-1688d83a8f62.png">

EXAMPLE 2 (stock experiencing a drastic price drop):
<img width="1278" alt="screen shot 2018-08-02 at 10 00 46 pm" src="https://user-images.githubusercontent.com/16903793/43620227-a93165fe-969f-11e8-9f86-e7d8c6b97b74.png">

<img width="1280" alt="screen shot 2018-08-02 at 10 01 03 pm" src="https://user-images.githubusercontent.com/16903793/43620232-b22cb262-969f-11e8-9eab-26e0f1559802.png">

The inspiration for this app stems from my personal curiosity to learn more about short-term price fluctuations in the stock
market, and how external forces (e.g. Amazon acquiring Whole Foods) can affect invester confidence.  This is a personal
side project I did for my own learning, and thus may not run perfectly.

IMPLEMENTATION
--------------
I used data from 2 external services to obtain the information I needed to build this app:

1.) Alpha Vantage - A service that provides time series APIs for both real-time and historical stock data.  I use stock data from this service formatted in Pandas-style dataframes to perform any data analysis. <br>
2.) NewsAPI.org - A service that provides JSON data for news articles pertaining to a particular topic.

I also used the scientific graphing libraries provided by "Plotly" to dynamically generate a URL, which is embedded within the HTML to display the stock chart.

Technology Stack: The majority of this program (including application logic) was written using Python.

Front-End: Standard HTML/CSS <br>
Back-End: Python Flask Server

I am the sole contributor to this app.

USING THE APP
--------------
Clone the repository, then add requirements from requirements.txt.  Type "flask run" to run the app, then open a browser and head to address 
'http://127.0.0.1:5000/' in your browser.

Because of the call limits on the free versions of the Alpha Vantage and Plotly APIs, the form requires that the user enter their
API keys.  These can easily be obtained at: 

1.) Alpha Vantage: https://www.alphavantage.co/support/#api-key <br>
2.) Plotly: https://plot.ly/settings/api#/

Upon reaching the homage, enter information for the name of the company you are interested in analyzing via the fields 'Company Name', Company's 'stock name', and your API keys.

