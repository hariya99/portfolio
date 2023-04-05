from backend import create_app, db 
from backend.models import User, UserDetails

app = create_app()

def create_tables():
    with app.app_context():
        db.drop_all()
        db.create_all()

def drop_tables():
    with app.app_context():
        db.drop_all()


def create_user(name: str, email: str):
    with app.app_context():
        u1 = User(username=name, email=email)
        db.session.add(u1)
        db.session.commit()

def create_user_details(usr: User, 
                        f_name: str, 
                        l_name: str, 
                        about: str):
    with app.app_context():
        u1 = UserDetails(first_name=f_name, 
                         last_name=l_name, 
                         about=about,
                         user_id=usr.id)
        db.session.add(u1)
        db.session.commit()

def list_users():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(user)


def create_first_user():
    with app.app_context():
        create_tables()
        create_user("dhruv", 
                    "dhruvagar29@gmail.com"
                    )
        u = User.query.filter_by(username="dhruv").first()
        create_user_details(u, 
                            "Dhruv",
                            "Agarwal",
                            "I am a software engineer."
        )

def run_tests_db():
    with app.app_context():
        create_tables()
        create_user("dhruv", 
                    "dhruvagar29@gmail.com"
                    )
        u = User.query.filter_by(username="dhruv").first()
        create_user_details(u, 
                            "Dhruv",
                            "Agarwal",
                            "I am a software engineer."
        )
        ud1 = UserDetails.query.first()
        print(u)
        print(ud1)
        drop_tables()

if __name__ == "__main__":
    # run_tests_db()
    # create_first_user()
    list_users()