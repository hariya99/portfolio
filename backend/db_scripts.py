import os
from backend import create_app, db 
from backend.models import User, UserDetails, Portfolio

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
                        intro: str, 
                        about: str):
    with app.app_context():
        u1 = UserDetails(first_name=f_name, 
                         last_name=l_name,
                         intro=intro, 
                         about=about,
                         user_id=usr.id)
        db.session.add(u1)
        db.session.commit()

def read_image(image_path: str):
    with open(image_path, "rb") as image_file:
        im_blob = image_file.read()
    return im_blob

def create_user_portfolio(usr: User):
    debias = {
            "image" :read_image("./backend/static/portfolio/debias.png"),
            "title" : 'Debiasing the Word Embeddings',
            "url" : 'https://github.com/dhruvagarwal29/Debiasing-Word-Embeddings.git' 
        }
    ethereum = {
            "image":read_image("./backend/static/portfolio/Ethereum.jpeg"),
            "title": 'Ethereum Transactions and Balance Using Etherscan API' ,
            "url":'https://github.com/dhruvagarwal29/Track-Ethereum-Transactions-and-Balance-Using-Python'
        }
    residual = {
            "image":read_image("./backend/static/portfolio/Residual.png"),
            "title": 'Implemented Deep learning residual networks' ,
            "url":'https://github.com/dhruvagarwal29/Residual-Network'
        }
   
    with app.app_context():
        p1 = Portfolio(image=debias["image"],
                       title=debias["title"], 
                         url=debias["url"],
                         user_id=usr.id)
        db.session.add(p1)
        p1 = Portfolio(image=ethereum["image"],
                       title=ethereum["title"], 
                         url=ethereum["url"],
                         user_id=usr.id)
        db.session.add(p1)
        p1 = Portfolio(image=residual["image"],
                       title=residual["title"], 
                         url=residual["url"],
                         user_id=usr.id)
        db.session.add(p1)
        db.session.commit()

                      
def list_users():
    with app.app_context():
        # users = User.query.all()
        # for user in users:
        #     print(user)
        u = User.query.filter_by(username="dhruv").first()
        print(u)
        ud = UserDetails.query.filter_by(user_id=u.id).first()
        print(ud)
        p = Portfolio.query.filter_by(user_id=u.id).all()
        for i in p:
            print(type(i.image))


def create_first_user():
    intro = [
            "I'm a Software Engineer and NYU Computer Engineering graduate seeking", 
            " full-time opportunities.", 
            " My passion lies in Machine Learning, Software Development, and Web Applications."
    ]
    about = [
            "I am a Computer Engineering Graduate student at New York University,",
            " with a strong focus on Machine Learning, Software Development,",
            " and Web Applications. My education includes a", 
            " Master of Science in Computer Engineering with a GPA of 3.8.", 
            " I have a diverse range of technical skills,", 
            " including proficiency in Python, Java, C, C++, HTML, CSS,", 
            " JavaScript, React, SQL, Shell Scripting, MySQL, and various",
            " libraries/tools.",
            " My professional experience includes a research internship with",
            " Cosmos Technology, where I conducted in-depth research on", 
            " cryptocurrencies and Metaverses and built a large-scale containerized",
            " database of scraped cryptocurrencies on AWS. I have also worked as", 
            " a Software Engineer Intern at Rice Lake Weighing System," 
            " where I developed and implemented a user-friendly configuration menu",
            " for a Linux-based indicator using JavaScript. Moreover,", 
            " I have worked as an Associate Application Developer at Accenture," 
            " where I developed a SAP PP system for monitoring the production of", 
            " coal."
            ]
    
    with app.app_context():
        create_tables()
        create_user("dhruv", 
                    "dhruvagar29@gmail.com"
                    )
        u = User.query.filter_by(username="dhruv").first()
        create_user_details(u, 
                            "Dhruv",
                            "Agarwal",
                            "".join(intro),
                            "".join(about)
        )
        create_user_portfolio(u)

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
    # create_tables()
    # create_first_user()
    list_users()