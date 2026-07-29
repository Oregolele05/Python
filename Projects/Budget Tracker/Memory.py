import csv
import os

class ExpenseCategory:
    def __init__(self, name, filename, fieldnames):
        self.name = name
        self.filename = filename
        self.fieldnames = fieldnames
        self.entries = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, newline='') as f:
                reader = csv.reader(f)
                next(reader, None)  # skip the category-name row
                next(reader, None)  # skip the fieldnames row
                for row in reader:
                    if row:
                        self.entries.append(row)

    def add_entry(self, entry):
        self.entries.append(entry)

    def save(self):
        with open(self.filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.name])
            writer.writerow(self.fieldnames)
            writer.writerows(self.entries)
            writer.writerow([])