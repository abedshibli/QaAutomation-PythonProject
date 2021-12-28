import csv


class DDT:
    my_list = []
    @staticmethod
    def write_to_list_from_csv():
        with open('C:\Automation\Hackaton python\Hackathon-Python\Test\db.csv', newline='') as f:
            reader = csv.reader(f)
            my_list = [tuple(row) for row in reader]
            return my_list
