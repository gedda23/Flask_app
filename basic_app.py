from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm


app = Flask(__name__)

app.config['SECRET_KEY']  = 'f317c285aa7af6fc5a7fa994f5ab7ca3'

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

@app.route("/hello")
def home():
    return render_template('Hello.html',posts=posts)

@app.route("/about")
def about():
    return render_template('About.html',title='About')

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","Success")
        return redirect(url_for('home')) 
    return render_template('register.html',title='Register',form=form)

@app.route("/login") 
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)


if __name__ == "__main__":
    app.run(debug=True)