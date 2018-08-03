Author: Nicholas A. Ficeto <br>
Date: 2018/08/02

OVERVIEW
--------
The purpose of this app is to demonstrate the myriad ways that real-world events can affect stock prices.  To achieve this, 
I've created an interface that combines a stock chart displaying closing prices over a 100-day span (Fig 1) along with news articles
corresponding to certain dates, like the day of the biggest drop in the stock's price (Fig 2) -- currently this is the only "special date" I have implemented.

Fig 1:
<img width="1279" alt="screen shot 2018-08-02 at 9 22 00 pm" src="https://user-images.githubusercontent.com/16903793/43619110-3bb0c4d4-969a-11e8-8bbe-ac8d27d7ffa1.png">

Fig 2:
<img width="1280" alt="screen shot 2018-08-02 at 9 07 17 pm" src="https://user-images.githubusercontent.com/16903793/43618981-91129e6c-9699-11e8-8b23-f1bdf3b6f0bc.png">

The inspiration for this app stems from my personal curiosity to learn more about short-term price fluctuations in the stock
market, and how external forces (e.g. Amazon acquiring Whole Foods) can affect invester confidence.  This is a personal
side project I did for my own learning, and thus may not run perfectly.

IMPLEMENTATION
--------------
I used 3 external services to obtain the information I needed to build this app: <br>
1.) Alpha Vantage - A service that provides time series APIs for both real-time and historical stock data.  I use stock data from this service formatted in Pandas-style dataframes to perform any data analysis. <br>
2.) NewsAPI.org - A service that provides JSON data for news articles pertaining to a particular topic. <br>
3.) Plotly - A service that provides scietnific graphing libraries.  Based off of the user-inputted stock name, I dynamically generate
a URL which is added to the HTML, and subsequently embeds the stock chart created from Plotly's website.

Technology Stack: The majority of this program (including application lgoic) was written using python.


Front-End: Standard HTML/CSS <br>
Back-End: Python Flask Server


I am the sole contributor to this app.
