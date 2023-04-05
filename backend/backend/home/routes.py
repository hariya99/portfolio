# Import flask and datetime module for showing date and time
from flask import Blueprint

# local imports
from backend.models import User, UserDetails

home = Blueprint('home', __name__)

# Route for seeing a data
@home.route('/home')
def get_time():

	user = User.query.filter_by(username="dhruv").first()
	details = UserDetails.query.filter_by(user_id=user.id).first()
	# Returning an api for showing in reactjs
	return {
		"first_name" : details.first_name,
		"last_name" : details.last_name,
		'about': details.about,
		}

