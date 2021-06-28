# importing all the dependencies
import os
import time
import pandas as pd
from flask import Flask
app = Flask(__name__)
#Index Page
@app.route("/")
def index():
    str='Click on the below url to access the table and count<br/>https://inlinemarket.azurewebsites.net/RowCount<br/>Click on the below url to access the date when the csv file was modified<br/>https://inlinemarket.azurewebsites.net/TimeStamp'
# I have used this route to generate the table and give the row count
@app.route("/RowCount")
def table():
    rm_quote = lambda x: x.replace('"', '')
    df = pd.read_csv("/inmk/airtravel.csv",doublequote=False,converters={'\"1958\"': rm_quote,'\"1959\"': rm_quote,'\"1960\"': rm_quote})
    df = df.rename(columns=rm_quote)
    return df.to_html(show_dimensions=True)
# I have used this route to generate the last time the csv file was modified
@app.route("/TimeStamp")
def pathtime():
    modTimesinceEpoc = os.path.getmtime("/inmk/airtravel.csv")
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
    message = "The file was last modified at :"
#    return modificationTime
    return  '{} {}'.format(message, modificationTime)
         

if __name__ == '__main__':
    app.run(debug=False,use_reloader=True)
