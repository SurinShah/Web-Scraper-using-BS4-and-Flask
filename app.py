import requests
import re
from bs4 import BeautifulSoup
from flask import Flask,render_template,request,redirect,url_for,Response
from urllib.parse import urlparse

app = Flask(__name__)

global lst 
lst =[]

@app.route('/')
def xyz():
    return render_template("index.html")

@app.route('/index',methods=["POST"])
def index():
    if request.method == 'POST':
        site = request.form.get["url"]
        o = urlparse(site)
        print(type(o))
        # r = requests.get(site)
        htmlContent = o.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        keywords = request.form["keywords"]
        print(keywords)
        print(site)
        # s = requests.get(keywords)
        # print(s)
        # print(type(s))
        keywrd= keywords.split(',')
        for i in range(len (keywrd)):
            keywrd[i].replace(" ","")
        for i in range (len(keywrd)):
            ref=soup.find_all(string=re.compile(keywrd[i]))
            lst.append(ref)
    return render_template("result.html",lst=lst)

@app.route('/result', methods=["POST"])
def result():
    lst=request.form.get("lst")
    return render_template('result.html', lst=lst)


if __name__ == '__main__':
    app.run(debug=True)


