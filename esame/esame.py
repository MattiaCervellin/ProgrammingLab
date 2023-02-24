class ExamException(Exception):
    pass

class CSVFile():

    def _init_(self,name):
        self.name=name #inizializzo nome file
        
    
    
    def get_data(self):
        data=[]
        try: 
            file=open(self.name, 'r')
        except:
            raise ExamException('Errore: impossibile aprire il file')
        for line in file:
            if line == 'date,passengers':
                elements = None
            else:
                line = line.strip('\n')
                elements = line.split(',')
                data.append(elements)
        file.close()
        return data



class CSVTimeSeriesFile(CSVFile):


    def get_data(self):
        string_data=super().get_data() #chiamo la funzione dalla classe padre
        
        if not string_data:                                       #lista vuota
            raise ExamException('Errore: lista vuota')
        
        
        numerical_data=[]     #mi assicuro di avere una lista utilizzabile

        for item in string_data:

            if item is not list:        #controllo che sia una lista di liste
                continue

            if len(item)!=2:         #controllo che le liste abbiano 2 elementi 
                continue
            
            data = item[0].split('-')  #creo la lista data fatta da anno e mese

            

            try:              #controllo che la data sia fatta da interi
                anno = int(data[0])
                mese = int(data[1])
            except ValueError:
                continue

            if item == string_data[0]:
                prev_year = data[0]  
                prev_month = data[1]
            else:                  #controllo se i timestamp sono duplicati o disordinati
                if data[0]<prev_year:
                    raise ExamException('Errore: timestamp non valido') 
                if data[0]==prev_year and data[1]<=prev_month:
                    raise ExamException('Errore: timestamp non valido')
                prev_year=data[0]
                prev_month=data[1]
            
                

            
            try:              #controllo che il numero dei passeggeri sia intero
                passeggeri = int(item[1])
            except ValueError:
                continue
                
            if anno>0 and mese>0 and mese<12 and passeggeri>0:  #controllo che la data sia possibile
                numerical_data.append(item)
                
            else:
                pass


            return numerical_data    #ho creato una lista con solo dati che posso utilizzare
        


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

def detect_similar_monthly_variations(time_series, years):

        #analizzo casi in cui il programma non potrebbe procedere
    
    if time_series==[]:            
        raise ExamException('Errore: time_series è vuoto')

    if years is not list:
        raise ExamException('Errore: years non è una lista')

    if years==[] or len(years)!=2:
        raise ExamException('Errore: years non adatto')

    try:
        int(years[0])
        int(years[1])
    except:
        raise ExamException('Errore: gli anni non sono interi')        


    
    var1=False   #questa variabile mi dirà se years si trova nella time_series

    lista1=[]
    for element in time_series:
        data = element[0].split('-')
        if data[0]==years[0]:
            var1=True
            #creo lista con valori in un anno, tenendo conto solo dei mesi a disposizione
            lista1.insert(data[1]-1, int(element[1])) 
    if var1==False:
        raise ExamException('Errore: anno non trovato')

        
        

    var2=False    #stessa cosa ma per il secondo anno

    lista2=[]
    for element in time_series:
        data = element[0].split('-')
        if data[0]==years[1]:
            var2=True
            lista2.insert(data[1]-1, int(element[1]))
    if var2==False:
        raise ExamException('Errore: anno non trovato')


    
    
    
    
    
    diff1=[]                       #creo le due liste differenza e ci metto dentro None oppure la                                         differenza tra 2 mesi
    for i in lista1:
        
        if i == lista1[0]:
            prev_value=i
        else:
            if i == None or prev_value == None:
                diff1.append(None)
                
            else:
                diff = int(i - prev_value)
                prev_value=i
                diff1.append(diff)

    diff2=[]
    for i in lista2:
        
        if i == lista2[0]:
            prev_value=i
        else:
            if i == None or prev_value == None:
                diff1.append(None)
            
            else:
                diff = int(i - prev_value)
                prev_value=i
                diff2.append(diff)


    
    variazioni = []                                    #creo la lista finale
    for i in enumerate(10):
        if diff1[i]==None or diff2[i]==None:           #se una diff vale None, non c'è il mese,                                                               quindi deve appare come False
            diff=1
        else:
            diff = diff1[i] - diff2[i]
        if diff>=-2 and diff<=2:
            variazioni.append(True)
        else:
            variazioni.append(False)
    return variazioni 
    
            

            
    



