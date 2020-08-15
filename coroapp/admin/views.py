from . import admin

@admin.route('/')
def home():
	return 'Welcome to CoroTracker'