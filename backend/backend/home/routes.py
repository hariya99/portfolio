from base64 import encodebytes
# Import flask and datetime module for showing date and time
from flask import Blueprint

# local imports
from backend.models import User, UserDetails, Portfolio

home = Blueprint('home', __name__)

# Route for seeing a data
@home.route('/home')
def get_time():

	user = User.query.filter_by(username="dhruv").first()
	details = UserDetails.query.filter_by(user_id=user.id).first()
	portfolio = Portfolio.query.filter_by(user_id=user.id).all()
	portfolio_list = []
	for i, p in enumerate(portfolio):
		portfolio_list.append({
			"id" : i + 1,
			"image": encodebytes(p.image).decode('ascii'),
			"title": p.title,
			"url": p.url
			})
	# Returning an api for showing in reactjs
	return {
		"first_name" : details.first_name,
		"last_name" : details.last_name,
		"intro" : details.intro,
		'about': details.about,
		"portfolios" : portfolio_list
		}

