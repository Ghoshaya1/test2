import os
import time
import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route("/")
def table():
    rm_quote = lambda x: x.replace('"', '')
    df = pd.read_csv("/inmk/airtravel.csv",doublequote=False,converters={'\"1958\"': rm_quote,'\"1959\"': rm_quote,'\"1960\"': rm_quote})
    df = df.rename(columns=rm_quote)
    return df.to_html(show_dimensions=True)

@app.route("/TimeStamp")
def pathtime():
    modTimesinceEpoc = os.path.getmtime("/inmk/airtravel.csv")
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
    time = print("Last Modified Time : ", modificationTime )
     
         

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
