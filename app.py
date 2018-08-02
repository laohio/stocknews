import requests
from flask import Flask, request, flash, render_template, redirect, url_for, session
from collections import defaultdict
from .stocks import Stock
from .forms import MainForm

# App config.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret key'

# Landing page with form to input required information (see MainForm object).  Data is sent via POST request.
@app.route("/",methods=['GET','POST'])
def index():
	form = MainForm(request.form)
	print(form.errors)
	

	if request.method == 'POST':
		session['stock_name'] = request.form['stock_name']
		session['company_name'] = request.form['company_name']
		session['alpha_key'] = request.form['alpha_key']
		session['plotly_key'] = request.form['plotly_key']
		if form.validate():
			return redirect(url_for('news'))
		else:
			flash('All form fields are required.')
	# GET request
	return render_template("index.html", form=form)

# Creates a stock object, then uses date of largest price drop to find news articles on that day.  Gets a URL to a Plotly graph
# which will be embedded in charts.html
@app.route("/news")
def news():
	# Instantiate stock class using the name of the stock entered, and API keys entered
	stock1 = Stock(session['company_name'], session['alpha_key'], session['plotly_key'])
	# Get the date that the stock dropped most in price, so that this can be used to get news articles in the News API
	date = stock1.getMaxDropDate()[1]
	print('THE DATE RETRIEVED IS: ',date)
	# Dictionary including top news articles' headlines and URLs on the day of the highest price drop
	articles_dict = getArticleData(session['company_name'], date)

	# Get the first 4 headlines text
	h1, h2, h3, h4 = articles_dict['h1'][0], articles_dict['h2'][0], articles_dict['h3'][0], articles_dict['h4'][0]
	# Get the first 4 headlines URLs
	h1_link, h2_link, h3_link, h4_link = articles_dict['h1'][1], articles_dict['h2'][1], articles_dict['h3'][1], articles_dict['h4'][1]	
	# Get Plotly graph URL for the stock name entered
	stock_url = stock1.getGraphURL()

	return render_template("charts.html",
		headline1=h1, headline2=h2, headline3=h3, headline4=h4,
		h1_link=h1_link, h2_link=h2_link, h3_link=h3_link, h4_link=h4_link,
		stock_url=stock_url
		)

# EXTERNAL API: NewsAPI.org
# Use the Python requests library to send a GET request to the NewsAPI.org servers, which will then return a JSON object containing
# information about the top news stories about the provided company/stock name on the date .
def getArticleData(company, date):
	url = 'https://newsapi.org/v2/everything?'
	# Parameters to add to query request.  'Company' and 'date' come from a.) user-entered company name and b.) date where the biggest drop
	# in stock price occured
	params = {'q':company,'from':date,'to':date,'domains':'wsj.com,bbc.com,nytimes.com,ft.com,economist.com','apiKey':'82a39149c286493492682aeafa7112e8',
	'language':'en'}
	# Get request to NewsAPI.og
	response = requests.get(url,params=params)
	# If successful:
	if response.status_code == 200:
		# 'article_data' represents the entire JSON metadata response.  Use the requests '.json()' method to "decode" the response
		article_data = response.json()
		# 'articles' is a list of data for the top articles in the JSON object
		articles = article_data['articles']
		# Call getHeadlines() to get a dictionary with the top 4 articles' text and URLs
		articles_dict = getHeadlines(articles)
		return articles_dict
	else:
		print('ERROR: ',response.status_code)

# Helper function for getArticleData().  Takes in a list of articles from the NewsAPI.org JSON object, and returns a dictionary: 
# keys = 'h1', 'h2', etc. (up to 'h4') and value = [title text of the article, URL]
def getHeadlines(articles):
	# List to store the headlines
	headlines = defaultdict(list)
	# Append either the top 4 headlines, or however many are available if there are not 4 available
	for i in range(1, min(5, len(articles)+1)):
		key = 'h' + str(i)
		headlines[key].append(articles[i-1]['title'])
		headlines[key].append(articles[i-1]['url'])
	return headlines


if __name__ == "__main__":
	app.debug=True
	app.run()