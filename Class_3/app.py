from flask import Flask , render_template,request

#instanciando
app = Flask(__name__,template_folder='./templates')

@app.route("/", methods = ['GET',])
def home():
  return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(400)
def bad_request(e):
    # note that we set the 400 status explicitly
    return render_template('400.html'), 400

@app.errorhandler(500)
def bad_request(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


if __name__ == "__main__":
  app.run( debug=True)