from flask import Flask, render_template, abort, request
from database import load_db, save_db, add_row, plot_crypto
import requests

app = Flask(__name__)
db = load_db("crypto_data.csv")


# Addition: This variable counts the number of
# visits of the 'data' page
counter = 0

@app.route("/")
def index():
    return render_template("index.html", columns=db.columns)


@app.route("/data")
def data():
    """
    Addition: data now counts the number of visits of the
    webpage (aka the number of times the page is accessed).
    To do this we need to define a variable counter outside
    the function and then update it inside the function by
    adding 1 each time the function is called (each time the
    page is visited).
    Because we cannot put counter in the function arguments nor
    in the return statement, we must explicitly tell Python that
    the counter variable updated inside the function is the one
    defined outside it (in the so-called global scope). For this
    reason we use the 'global' keyword.
    """

    global counter
    counter += 1

    return render_template('data.html', counter=counter)

# Addition: about_us.html (which inherits from html)
@app.route("/about_us")
def about_us():
    return render_template('about_us.html')

#/crypto/0 -> BITCOIN
#/crypto/1 -> DOGECOIN
#/crypto/2 -> ETHEREUM
@app.route("/crypto/<int:index>", methods=["GET", "POST"])
def crypto(index):
    if index >= len(db.columns):
        abort(404)
    
    if request.method == "POST":
        results = requests.get(
            'https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]')
        results = results.json()

        # Target: {"BITCOIN": 1, "DOGECOIN": 2, "ETHEREUM": 3}
        
        unformatted_row = {
            result["symbol"]: result["price"]
            for result in results
        }
        
        # Now we have: {"BTCUSDT": "1", "DOGEUSDT": "2", "ETHUSDT": "3"}
        column_map = {
            "BTCUSDT": "BITCOIN",
            "DOGEUSDT": "DOGECOIN",
            "ETHUSDT": "ETHEREUM"
        }
        new_row = {
            column_map[key]: float(value)
            for key, value in unformatted_row.items()
        }
        add_row(db, new_row)
        save_db(db, "crypto_data.csv")
        plot_crypto(db)

    name = db.columns[index]
    price = db[name].iloc[-1]
    plot_name = f"{name}_plot.png"

    # Addition: return the maximum index
    # (the number of columns -1).
    # See the template for detail
    return render_template(
        "crypto.html",
        name=name,
        value=price,
        plot_name=plot_name,
        index=index,
        max_index=len(db.columns) - 1
    )