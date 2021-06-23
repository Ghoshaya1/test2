import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route("/")
def table():
    rm_quote = lambda x: x.replace('"', '')
    df = pd.read_csv("/inmk/airtravel.csv",doublequote=False,converters={'\"1958\"': rm_quote,'\"1959\"': rm_quote,'\"1960\"': rm_quote})
    df = df.rename(columns=rm_quote)
    return df.to_html()
@app.route("/rowcount")
def rowcount():
    cf = pd.read_csv("/inmk/airtravel.csv",doublequote=False,converters={'\"1958\"': rm_quote,'\"1959\"': rm_quote,'\"1960\"': rm_quote})
    cf = index = cf.index
    number_of_rows = len(index)
    return 'The number of rows in the table is ', number_of_rows.to_html()
         

if __name__ == '__main__':
    app.run()
