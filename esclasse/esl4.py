class CSVFile():

    def __init__(self, name):
        self.name = name


    def get_data(self):
        data=[]
        file=open(self.name, 'r')
        for line in file:
            if line == 'Date,Sales\n':
                elements = None
            else:
                line = line.strip('\n')
                elements = line.split(',')
                data.append(elements)
        file.close()
        return data

file=CSVFile('shampoo_sales.csv')
print(file.get_data())

        
        


