from collections import OrderedDict


def csv_reader(file):
    decode_file = file.split('\n')

    for line in decode_file:
        d = line.split(',')
        if len(d) and any(d):
            yield iter(d)


class CustomReader:

    def __init__(self, file, fieldnames, pass_first=True):
        self.reader = csv_reader(file)
        self.line_num = 0
        self.pass_first = pass_first
        self.fieldnames = fieldnames

    def __iter__(self):
        return self

    def __next__(self):
        if self.pass_first and self.line_num == 0:
            _ = next(self.reader)

        row = next(self.reader)
        self.line_num += 1

        while row == []:
            row = next(self.reader)

        d = OrderedDict(zip(self.fieldnames, row))
        return d
