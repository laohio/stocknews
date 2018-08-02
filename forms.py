from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class MainForm(Form):
	# Name of company
	company_name = TextField('Company Name: ', validators=[validators.required()])
	# Stock symbol of company
	stock_name = TextField('Stock Symbol: ', validators=[validators.required()])
	# Alpha Vantage API Key
	alpha_key = TextField('Alpha Vantage API Key: ', validators=[validators.required()])
	# Plotly API key
	plotly_key = TextField('Plotly API Key: ', validators=[validators.required()])