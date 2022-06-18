import csv

class Books:
    def __init__(self, path):
        with open(path, 'r') as books:
            self.data = list(csv.DictReader(books))

    @property
    def by_category(self):
        result = {}
        for line in self.data:
            category = line.get('Genre', None)
            result[category] = result.get(category, []) + [line]
        return result
