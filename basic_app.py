from flask import Flask,render_template,url_for

app = Flask(__name__)

posts = [{
    'Author' :'Venkata Sai Aditya Gedda',
    'Title'  :'Blog Post1',
    'Content':'First Post Content'
},
{
    'Author' :'Ruthvik Ramaswamy',
    'Title'  :'Blog Post2',
    'Content':'Second Post Content'
}]

@app.route("/")
def home():
    return render_template('Hello.html',posts=posts)

@app.route("/about")
def about():
    return render_template('About.html',title='About')


if __name__ == "__main__":
    app.run(debug=True)