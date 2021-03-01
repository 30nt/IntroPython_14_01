import json

class JsonReader:
    def __init__(self, path_file):
        self._path_file = path_file
        self.data = None

    def __repr__(self):
        return str(self.data)

    def read_json(self):
        with open(self._path_file, 'r') as file:
            self.data = json.load(file)

    def sort(self):
        raise NotImplementedError


class JsonListReader(JsonReader):
    def __init__(self, path_file, float_mode):
        super().__init__(path_file)
        self._float_mode = float_mode

    def read_json(self):
        # super(JsonReader, self).__init__()
        super().read_json()
        if self._float_mode:
            self.data = list(map(float, self.data))

    def sort(self):
        self.data.sort()


class JsonDictReader(JsonReader):
    def sort(self):
        self.data = {dict_key[0]: self.data[dict_key[0]] for dict_key in sorted(self.data.items(), key=lambda x: x[1])}


json_data = JsonListReader("test_json.json", float_mode=True)
json_data.read_json()
json_data.sort()
print(json_data)

json_data = JsonDictReader("test_json_write.json")
json_data.read_json()
json_data.sort()
print(json_data)