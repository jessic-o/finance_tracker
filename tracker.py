import csv
from datetime import datetime
from pathlib import Path


class Transaction:
    def __init__(self, amount: float, category: str, description: str, date: str = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
        }


class FinanceTracker:
    def __init__(self, filename="transactions.csv"):
        self.filename = Path(filename)
        self.transactions = []
        self.load_transactions()

    def add_transaction(self, amount: float, category: str, description: str = ""):
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.save_transactions()

    def get_balance(self) -> float:
        return sum(t.amount for t in self.transactions)

    def get_summary(self):
        categories = {}
        for t in self.transactions:
            categories[t.category] = categories.get(t.category, 0) + t.amount
        return categories

    def save_transactions(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "amount", "category", "description"])
            writer.writeheader()
            for t in self.transactions:
                writer.writerow(t.to_dict())

    def load_transactions(self):
        if self.filename.exists():
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                self.transactions = [
                    Transaction(float(row["amount"]), row["category"], row["description"], row["date"])
                    for row in reader
                ]
