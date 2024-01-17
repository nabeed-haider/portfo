from flask import Flask,render_template # importing Flask class to initiate a flask web app/server for the matter
from flask import request,redirect # importing request and redirect methods to grab data from the user and redirect to a new webpage
import csv
app = Flask(__name__)

@app.route('/') # root/home directory
def home():
   return render_template('./index.html')



@app.route('/<string:page_name>')
 # any .html file , basically we can define a param in the following function that is string data type


def html_page(page_name):
    return render_template(page_name)



@app.route('/submit_form', methods=['POST', 'GET'])
# we have to methods for this kind of url 'POST' and 'GET'

# POST -> if user posts something

# if we ever reach a submit form 
def submit_form():
    if request.method == 'POST':
        # if data is entered by the user
        try:
            data = request.form.to_dict() # converts given data into a dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database."
    else:
        return 'try again'

def write_to_file(data):
    # file handling-txt file
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    # file handling-csv file
    with open('database.csv',newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

