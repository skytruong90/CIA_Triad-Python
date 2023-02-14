import hashlib

class CIA_Triad:
    def __init__(self, data):
        self.data = data
        self.hash = hashlib.sha256(data.encode('utf-8')).hexdigest()

    def confidentiality(self):
        return self.hash

    def integrity(self):
        return hashlib.sha256(self.data.encode('utf-8')).hexdigest()

    def availability(self):
        return len(self.data)
