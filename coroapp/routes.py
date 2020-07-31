from flask import Flask, render_template, flash, url_for
from coroapp import app
@app.route('/')
def home():
	return 'Welcome to CoroTracker'