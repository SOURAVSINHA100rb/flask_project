from flask import Flask, render_template

HOST = "localhost"
PORT = 5000
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Solution Architect',
        'location': 'New Delhi, India',
        'salary': '4-5LPA'
    },
    {
        'id': 2,
        'title': 'Python Developer',
        'location': 'New Delhi, India',
        'salary': '10-15 LPA'
    },
    {
        'id': 3,
        'title': 'React Developer',
        'location': 'New Delhi, India',

    }
]


@app.route("/")
def home_page():
    return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
