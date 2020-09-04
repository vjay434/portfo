import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_data(data)
    	csv_writer(data)
    	return redirect('/thankyou.html')
    else:
    	return 'Something went wrong!'

        
  def  write_data(data):
	with open('database.txt', mode ='a') as database:
		email = data["email"]
		subject = data["text"]
		message = data["message"]
		file = database.write(f'\n{email}, {subject}, {message}')


def csv_writer(data):
		
	with open('database.csv', 'a', newline='') as csvfile:
		email = data["email"]
		subject = data["text"]
		message = data["message"]
		spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([email,subject,message])
	    




# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def aboutme():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/comonents.html')
# def comonents():
#     return render_template('comonents.html')

# @app.route('/')
# def hello_world():
#     return render_template('index.html')


# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index.html', name=username)


# @app.route('/blog')
# def blog():
#     return 'welcome to the blog!'


# @app.route('/aboutme')
# def aboutme():
#     return 'contact us'