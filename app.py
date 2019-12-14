from flask import Flask, render_template, url_for

articles = {
	"title": "First post",
	"author": "Bastien Ratat",
	"date": "2019, December 14",
	"content": "waiting for being filled with interesting content"
}

pages = ["Homepage", "About", "Products"]

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", articles=articles, pages=pages)

@app.route('/about')
def about():
    return render_template("about.html", title='About', pages=pages)

@app.route('/products')
def products():
    return render_template("products.html", title='Our products', pages=pages)

if __name__ == '__main__':
	app.run(debug=True)
    
