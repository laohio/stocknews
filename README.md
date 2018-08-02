Author: Nicholas A. Ficeto
Date: 2018/08/02

OVERVIEW
--------
The purpose of this app is to demonstrate the myriad ways that real-world events can affect stock prices.  To achieve this, 
I've created an interface that combines a stock chart displaying closing prices over a 100-day span along with news articles 
corresponding to certain dates (e.g. the day of the biggest drop in the stock's price -- currently this is the only date I have
implemented to make external API requests for news articles).

The inspiration for this app stems from my personal curiosity to learn more about short-term price fluctuations in the stock
market, and how big news announcements (e.g. Amazon acquiring Whole Foods) can affect invester confidence.  This is a personal
side project I did for my own learning, and thus may not run perfectly.

IMPLEMENTATION
--------------
I used 3 external services to obtain the information I needed to build this app:
1.) Alpha Vantage - A service that provides time series APIs for both real-time and historical stock data.  I use stock data from this service formatted in Pandas-style dataframes to perform any data analysis.
2.) NewsAPI.org - A service that provides JSON data for news articles pertaining to a particular topic.
3.) Plotly - A service that provides scietnific graphing libraries.  Based off of the user-inputted stock name, I dynamically generate
a URL which is added to the HTML, and subsequently embeds the stock chart created from Plotly's website.

Technology Stack: The majority of this program (including application lgoic) was written using python.


Front-End: Standard HTML/CSS
Back-End: Python Flask Server


I am the sole contributor to this app.