import csv

def read_csv(filename: str) -> list:
    with open(filename, 'r') as csv_file:
        data = []
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            data.append(row)
    return data


def write_csv(filename, data):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(data)


# print(__name__)
if __name__ == "__main__":
    data_2 = read_csv("test2.csv")
    print(data_2)