import pandas as pd
import matplotlib.pyplot as plt


def load_db(path):
    db = pd.read_csv(path)
    return db


def save_db(db, path):
    db.to_csv(path, index=False)


def add_row(db, row):
    new_index = len(db)
    db.loc[new_index] = row


def plot_crypto(db):
    for name in db.columns:
        db.plot(y=name, use_index=True, marker="o")
        plt.xticks(range(len(db)))
        plt.xlabel("Measure")
        plt.ylabel("Price (USD)")
        plt.savefig(f"static/{name}_plot.png")



if __name__ == "__main__":
    db = load_db("crypto_data.csv")
    plot_crypto(db)
    print(db)
    add_row(db, [1, 1, 1])
    save_db(db, 'crypto2.csv')
