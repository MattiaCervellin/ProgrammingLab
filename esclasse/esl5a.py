class CSVFile():

    def __init__(self, name):
        self.name = name


    def get_data(self):
        data=[]
        try: 
            file=open(self.name, 'r')
        except:
            print('Errore: questo file non esiste')
        for line in file:
            if line == 'Date,Sales\n':
                elements = None
            else:
                line = line.strip('\n')
                elements = line.split(',')
                data.append(elements)
        file.close()
        return data

    
    