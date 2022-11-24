class CSVfile():

    def __init__(self, name):
        self.name = name


    def get_data(self):
        elements = []
        myfile = open(self.name, 'r')
        for line in myfile:
            list = split.()
            print(list)
        



def sum_csv(my_file):
    values = []
    fun = open(my_file, 'r')
    for line in fun:
        elements = line.split(',')
        if elements[0] != 'Date':
            #date = elements[0]
            value = elements[1]
            values.append(float(value))
    if len(values) == 0:
        return None
    somma = sum(values)

    return somma


print(sum_csv("shampoo_sales.csv"))
