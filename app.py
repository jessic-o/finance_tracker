from flask import Flask, render_template, request, redirect, url_for
from tracker import FinanceTracker
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
tracker = FinanceTracker()


@app.route("/")
def index():
    balance = tracker.get_balance()
    transactions = tracker.transactions
    return render_template("index.html", balance=balance, transactions=transactions)


@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]
        # Expenses stored as negative
        if request.form["type"] == "expense":
            amount = -abs(amount)
        tracker.add_transaction(amount, category, description)
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/summary")
def summary():
    categories = tracker.get_summary()

    # --- Generate Matplotlib chart ---
    if categories:
        plt.figure(figsize=(5, 5))
        plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
        plt.title("Expenses/Income by Category")
        chart_path = os.path.join("static", "chart.png")
        plt.savefig(chart_path)
        plt.close()
    else:
        chart_path = None

    return render_template("summary.html", categories=categories, chart=chart_path)


if __name__ == "__main__":
    app.run(debug=True)
