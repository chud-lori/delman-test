"""
run from python using flask run
"""

from app import create_app

# create instance app
app = create_app()

if __name__ == '__main__':
    # run in debug mode
    app.run(debug=False)