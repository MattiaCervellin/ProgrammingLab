class CSVfile():

    def __init__(self, name):
        self.name = name


    def get_data(self):
        data=[]
        file=open(self.name, 'r')
        for line in file:
            if line == 'Date,Sales\n':
                elements = None
            else:
                elements = line.split(',')
                data.append(elements)
        file.close()
        print (data)

file=CSVfile('shampoo_sales.csv')
file.get_data()

        
        


