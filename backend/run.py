from backend import create_app

if __name__ == "__main__":
    create_app().run(port=8000, debug=True)