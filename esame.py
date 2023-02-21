class ExamException(Exception):
    pass

class CSVFile():

    def _init_(self,name):
        self.name=name #inizializzo nome file
        self.can_read=True #provo ad aprire file e leggerlo
        
        try:
            my_file=open(self.name,'r')
            my_file.readline()
        except ExamException as e:
            self.can_read=False
            print('Errore, file non leggibile: {}'.format(e))
    
    
    def get_data(self):
        if not self.can_read:
            print('Errore, file non aperto o leggibile')
            return None
        
        else:
            data=[] #nuova lista vuota 
            my_file=open(self.name,'r') #apro il file
            for line in my_file:
                elements=line.split(',')
                elements[-1]=elements[-1].strip() #tolgo spazi bianchi e \n
                if elements[0]!='date':
                    data.append(elements) #aggiungo elementi alla lista 
            
            my_file.close()
            
            return data 



class CSVTimeSeriesFile(CSVFile):


    def get_data(self):
        string_data=super().get_data() #chiamo la funzione dalla classe padre
        
        if not string_data:                                       #lista vuota
            raise ExamException('Errore: lista vuota')
        numerical_data=[]     #mi assicuro di avere una lista utilizzabile

        for item in string_data:

            if item is not list:
                raise ExamException('Errore: string_data non è fatta di liste')
            
            data = item[0].split('-')  #creo la lista data fatta da anno e mese

            try:              #controllo che la data sia fatta da interi
                anno = int(data[0])
                mese = int(data[1])
            except ValueError:
                pass
                

            try:              #controllo che il numero dei passeggeri sia intero
                passeggeri = int(item[1])
            except ValueError:
                pass
                
            if anno>0 and mese>0 and mese<12 and passeggeri>0:  #controllo che la data sia possibile
                numerical_data.append(item)
                
            else:
                raise ExamException('Errore: data non valida')


            return numerical_data
        


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

def detect_similar_monthly_variations(time_series, years):





    lista1=[]
    for element in time_series:
        data = element[0].split('-')
        if data[0]==years[0]:
            
            lista1.insert(data[1]-1, int(element[1]))

    lista2=[]
    for element in time_series:
        data = element[0].split('-')
        if data[0]==years[1]:

            lista2.insert(data[1]-1, int(element[1]))


    
    
    
    
    
    diff1=[]
    for i in lista1:
        if i == lista1[0]:
            prev_value=i
        else:
            diff = int(i - prev_value)
            prev_value=i
            diff1.append(diff)

    diff2=[]
    for i in lista2:
        if i == lista1[0]:
            prev_value=i
        else:
            diff = int(i - prev_value)
            prev_value=i
            diff2.append(diff)










    variazioni = []
    for i in enumerate(10):
        diff = diff1[i] - diff2[i]
        if diff>=-2 and diff<=2:
            variazioni.append(True)
        else:
            variazioni.append(False)
    return variazioni 
    
            
        
    
            
            
    



