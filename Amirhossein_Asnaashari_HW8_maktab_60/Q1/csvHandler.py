import csv


class CSVHandler:
    def __init__(self, filename="myfile.csv"):
        self.filename = filename

    def write(self, rows):
        with open(self.filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            rows = map(str, rows)
            csvwriter.writerow(rows)

    def read(self):
        rows = []
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
        return rows, fields