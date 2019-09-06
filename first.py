from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "This is home page"

@app.route('/raunak')
def raunak():
    return'<h2> Raunak is awesome</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>hey there %s <h2>" % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>the age is %d<h2>" %post_id


if __name__ == "__main__":
    app.run(debug=True)
