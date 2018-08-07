from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    players=["messi", "ronaldo", "naimar"]
    return render_template("index.html", 
    players=players,
    like_same_sport=True)
def home_page():
    return "ballet"



if __name__ == '__main__':
   app.run(debug = True)