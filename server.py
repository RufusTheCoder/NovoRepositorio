from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index_new.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["assunto"]
		message = data["texto"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email = data["email"]
		subject = data["assunto"]
		message = data["texto"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		print(data)
		return redirect('/thank_you.html')
	else:
		return 'moio'
    # return render_template('login.html', error=error)


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/project.html')
# def project():
#     return render_template('project.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')



# 
    ########### Parking Lot ############
    # @app.route('/<username>')
# def usuario(username=Fulano):

# @app.route('/user/<username>/<int:post_id>')
# def show_user_profile(username=None, post_id=None):
# 	return render_template('index.html', name=username, postID = post_id)

# @app.route('/blog')
# def blogus():
#     return 'Blogus do Rufus'

# @app.route('/blog/postdorufus')
# def postus():
#     return 'Post do Rufus'


