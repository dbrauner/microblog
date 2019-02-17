from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Douglas'}
    posts = [
        {
            'author': {'username':'Douglas'},
            'body': 'Beatiful day in Sao Leopoldo!'
        },
        {
            'author': {'username':'Brunna'},
            'body': 'The Avengers movie was so cool'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
