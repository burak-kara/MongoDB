import csv


class DataReader:
    def __init__(self, path):
        self.path = path

    def prepare_model(self, columns, row):
        model = {}
        i = 0
        while i < len(row):
            model[columns[i]] = row[i]
            i += 1
        return model

    # read dataset
    def read_csv_data(self):
        columns = []
        data_model = []
        with open(self.path, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for i in range(len(row)):
                        columns.append(row[i])
                    line_count += 1
                else:
                    data_model.append(self.prepare_model(columns, row))
                    line_count += 1
        return data_model
