# Time series API from Alpha Vantage.  We use a Python wrapper for convenience.  
from alpha_vantage.timeseries import TimeSeries
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# Graphing library for advanced stock charts
import plotly as plotly
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime

# Class which represents a stock and its daily prices over a ~100 day span (as per Alpha Vantage data).  The class takes in a particular stock
# name as an argument, as well as an API key to make requests to AV and an API key to make requests.  Upon initialization, this stock name is used 
# to make a request to Alpha Vantage's servers, which returns a Pandas-style dataframe to represent the data (note: this process is abstracted 
# via the Alpha Vantage Python module).
class Stock(object):
	def __init__(self, stock_name, alpha_key, plotly_key):
		# Initialize the stock's name as a member variable
		self.name = stock_name
		# Set Alpha Vantage API key as a member variable
		self.alpha_key = alpha_key
		# Initialize the Pandas-style self.dataframe for the stock's by calling "getGraphself.data" function.
		self.data, self.meta_data = self.getDataFrameData()
		# Set plotly credentials
		self.plotly_key = plotly_key
		plotly.tools.set_credentials_file(username='laohio', api_key=self.plotly_key)

	# EXTERNAL API: ALPHA VANTAGE TIME SERIES API
	# Retrieve data for the given stock.  Comes formatted in a Pandas-style dataframe which includes the stock's opening price, closing price,
	# and more over the past 100 days.
	# Currently using my own API key (consider requiring someone else provide their own when testing application)
	def getDataFrameData(self):
		# Pass in personal API key, initialize Alpha Vintage time series object.  Here we choose to display the self.data using a Pandas-style
		# dataframe, though JSON is an alternative choice.
		ts = TimeSeries(key=self.alpha_key,output_format='pandas')
		# Get 1.) json object with interday self.data and 2.) json object with the call's metadata
		self.data, self.meta_data = ts.get_daily(self.name)
		return self.data, self.meta_data

	# Find the date with the biggest drop in price.  Return a tuple containing 1.) the index of the price drop and 2.) the date itself
	# as a string
	def getMaxDropDate(self):
		smallest_gap = 0
		date_index = 0
		for i in range(1, len(self.data)):
		    close_today, close_yesterday = self.data.iloc[i]['4. close'], self.data.iloc[i-1]['4. close']
		    if close_today < close_yesterday:
		        if close_today - close_yesterday < smallest_gap:
		            date_index = i
		            smallest_gap = close_today - close_yesterday
		return (date_index, self.data.iloc[date_index][3])

	# Get the four coordinates (2 points on graph) whose line represents the biggest price drop of the stock within the 
	# time period.  Call getMaxDropDate() to get the index of the date with the biggest price drop
	def getMaxDropCoordinates(self):
		date_index = self.getMaxDropDate()[0]
		# Pre and post max price drop
		drop = self.data.iloc[date_index-1:date_index+1]

		# Reset the index of the dataframe to allow easier access of the date of the drop
		self.data.reset_index(inplace=True)
		# Get x coordinates as date strings
		x1,x2 = self.data['date'][date_index-1], self.data['date'][date_index]
		# Get y coordinates as prices
		y1, y2 = drop.iloc[0]['4. close'], drop.iloc[1]['4. close']

		
		return x1, y1, x2, y2

	# EXTERNAL API: Plotly graphing library
	# Get the plotly URL which will allow us to embed the graph into charts.html
	def getGraphURL(self):
		# Get the coordinates of the two dates where the maximum price drop occured
		x1, y1, x2, y2 = self.getMaxDropCoordinates()
		# Stock prices time series data
		trace1 = go.Candlestick(x=self.data['date'],
		                       name='Stock Price',
		                       open=self.data['1. open'],
		                       high=self.data['2. high'],
		                       low=self.data['3. low'],
		                       close=self.data['4. close'],
		                       increasing=dict(line=dict(color= '#17BECF')),
		                       decreasing=dict(line=dict(color= '#7F7F7F')))
		# Line representing the drop in stock price
		trace2 = go.Scatter(
		    x=[x1, x2],
		    y=[y1, y2],
		    mode='lines+text',
		    name='Largest Overnight Drop',
		    text=['close 1', 'close 2'],
		    textposition='top center'
		)
		# Title of the stock chart
		title = self.name + ' Daily Stock Prices'
		# Details for the title and axes
		layout = go.Layout(
		    title=title,
		    xaxis=dict(
		        title='Date',
		        titlefont=dict(
		            family='Courier New, monospace',
		            size=18,
		            color='#7f7f7f'
		        )
		    ),
		    yaxis=dict(
		        title='Stock Price',
		        titlefont=dict(
		            family='Courier New, monospace',
		            size=18,
		            color='#7f7f7f'
		        )
		    )
		)

		data = [trace1,trace2]
		fig = go.Figure(data=data, layout=layout)
		# Get the URL for which the stock chart can be embedded into HTML
		stock_chart_url = py.plot(fig, filename='simple_candlestack',auto_open=False)
		return stock_chart_url