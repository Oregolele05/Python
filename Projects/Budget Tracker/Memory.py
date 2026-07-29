import csv
import os
import traceback

class ExpenseCategory:
    """
    A generic class to manage expense entries for a single category.
    All data is stored in a CSV file inside the 'Files' subfolder.
    """

    def __init__(self, name, filename, fieldnames):
        """
        :param name: Human‑readable category name (used as a header in the CSV)
        :param filename: Base filename (e.g., "debt_payments.csv")
        :param fieldnames: List of column headers for the CSV
        """
        self.name = name
        self.fieldnames = fieldnames
        self.entries = []

        # Always use the 'Files' subfolder relative to this script
        base_dir = os.path.dirname(__file__)
        folder = os.path.join(base_dir, "Files")
        os.makedirs(folder, exist_ok=True)          # ensure folder exists
        self.filename = os.path.join(folder, filename)

        self.load()

    def load(self):
        """Load existing data from the CSV file (if it exists)."""
        if not os.path.exists(self.filename):
            return  # no file yet – start with empty entries

        try:
            with open(self.filename, newline='') as f:
                reader = csv.reader(f)
                # Skip the category‑name row
                next(reader, None)
                # Skip the fieldnames row
                next(reader, None)
                # Read all data rows
                for row in reader:
                    if row:   # skip empty lines
                        self.entries.append(row)
        except OSError as e:
            print(f"⚠️ Could not load {self.filename}: {e}")
            traceback.print_exc()
            # Continue with empty entries – the user can re‑enter data

    def add_entry(self, entry):
        """
        Add a new expense entry.
        `entry` must be a list of values in the same order as `fieldnames`.
        """
        self.entries.append(entry)

    def save(self):
        """Write all entries back to the CSV file."""
        try:
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([self.name])
                writer.writerow(self.fieldnames)
                writer.writerows(self.entries)
                writer.writerow([])   # trailing blank line for readability
        except OSError as e:
            print(f"❌ Could not save {self.filename}: {e}")
            traceback.print_exc()

    def get_total(self):
        """
        Convenience method: sum the last column of each entry.
        Assumes the last field is the amount (in Rands).
        Override if your CSV structure is different.
        """
        total = 0.0
        for row in self.entries:
            try:
                # The last column is assumed to be the amount
                total += float(row[-1])
            except (ValueError, IndexError):
                # Skip malformed rows
                continue
        return total