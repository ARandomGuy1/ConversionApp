from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route("/p3")
def render_page3():
    return render_template('page3.html')

  
@app.route("/response")
def render_response():
    foot = request.args['foot']
    return render_template('response.html', response = float(foot)*30.48)
                      
@app.route("/response2")
def render_response2():
    foot = request.args['foot']
    return render_template('response.html', response2 = float(foot)*30.48)

@app.route("/response3")
def render_response3():
    foot = request.args['foot']
    return render_template('response.html', response3 = float(foot)*30.48)
  
if __name__=="__main__":
    app.run(debug=False, port=54321)
