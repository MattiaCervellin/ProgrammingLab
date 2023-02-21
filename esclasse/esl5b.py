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



class NumericalCSVFile(CSVFile):

    def get_data(self):
        
        string_data=super().get_data()
        numerical_data = []

        for string_row in string_data:
            numerical_row = []

            for i,element in enumerate(string_row):

                if i==0:
                    numerical_row.append(element)

                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break


            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data            
                        
                        
            
            
        
    

    