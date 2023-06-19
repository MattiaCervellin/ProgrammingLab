class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    
    def __init__(self,name):
        
        self.name=name 
            
    def get_data(self):
        
        #controllo nome
        if self.name is None:
            raise ExamException('Errore: nome file non inserito in input!')

        #provo ad aprire e chiudere il file
        try:
            my_file=open(self.name, 'r')
            my_file.readline()
            my_file.close()
        except Exception:
            raise ExamException('Errore: non è stato possibile aprire o leggere il file!')

        #lista vuota per salvare i dati alla fine
        lista=[]
        
        #riapro il file
        my_file=open(self.name, 'r')

        #leggo il file linea per linea
        for line in my_file:

            
            #pulizia carattere dall'ultimo elemento e split sulla virgola
            elements=line.strip("\n").split(",")
            
            

            #salto la prima riga
            if elements[0].strip() == 'date':
                continue

            #variabile ausiliara per fare un check su anni e mesi
            tempo=elements[0].split('-') 
            

            

            try:
                tempo[0] = int(tempo[0])
                tempo[1] = int(tempo[1])
            except Exception:
                continue

            
            try:
                passengers=int(elements[1])
            except Exception:
                continue

            if passengers<=0:
                continue
                            
            #aggiungo alla lista gli elementi di questa linea con la data sotto forma di stringa e il numero di passeggeri
            
            lista.append(elements)

        #se arrivo al comando append vuol dire che la riga del file va bene. atrimenti viene saltata senza alzare eccezioni
        
        #chiudo il file
        my_file.close()

        #controllo la validità dei dati(ordine e duplicazioni varie)
        numerical_data=[]
        for item in lista:
            if item == []:
                continue
            if len(item) < 2:
                continue  #la lista deve avere almeno due valori (data e numero passeggeri)

            #controllo che i valori siano interi
            tempo = item[0].split('-')  #separo anno e mese
            try:
                anno = int(tempo[0])  #anno è un intero
                mese = int(tempo[1])  #mese è un intero
                passeggero = int(item[1])  #passeggero è un intero
            except Exception:
                continue

            #controllo che i dati siano ordinati per aggungerli a numerical_data
            if item == lista[0]:
                prev_anno = anno
                prev_mese = mese
            else:
                if anno < prev_anno:
                    raise ExamException('errore, anni non ordinati')
                    continue
                if mese <= prev_mese and anno == prev_anno:
                    raise ExamException('errore, mesi non ordinati o duplicati')
                    continue
                prev_anno = anno
                prev_mese = mese
            if anno > 0 and mese > 0 and mese <= 12 and passeggero >= 0:
                numerical_data.append(item)

        return numerical_data
        
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
#print(time_series)

#################################################################################

#FUNZIONE PER IL CALCOLO DELLA FIFFERENZA MENSILE MEDIA

def compute_avg_monthly_difference(time_series, first_year, last_year):

    if not time_series:
        raise ExamException('Errore: time_series è vuota')
    
    
    
    #converto gli anni dati in input in interi
    try:
        anno1=int(first_year)
        anno2=int(last_year)
    except Exception:
        raise ExamException('Errore: impossibile convertire gli anni in input in interi')

    if anno1>anno2:
        raise ExamException('Errore: first_year>last_year')
    
    #controllo che primo e ultimo anno siano nella time_series
    found1=False
    found2=False
    
    #primo anno
    for element in time_series:
        
        time=element[0].split('-')
        year=time[0]

        if year==first_year:
            found1=True
            break
    
    #ultimo anno
    for element in time_series:
        
        time=element[0].split('-')
        year=time[0]

        if year==last_year:
            found2=True
            break

    #se alla fine non trovo gli anni, alzo un'eccezione
    if not found1 or not found2:
        raise ExamException('Errore: anni non presenti nella lista')

    
    
    
    
    #CREO LISTA DI LISTE, UNA PER ANNO, CON ALL'INTERNO TUTTI I DATI DELL'ANNO
    
    tot_anni=[]

    
    prev_anno=anno1

    
    year=[]
    for i in range(12):
        year.append(0)


    #Converto anno e mese in numeri interi
    for element in time_series:
        time = element[0].split('-')
        try:
            anno=int(time[0])
            mese=int(time[1])-1
            passeggeri=int(element[1])
        except:
            continue

        #considero solo l'intervallo di anni che ci interessa
        if anno < anno1 or anno > anno2:
            continue
        
        
        if anno==prev_anno:
            year[mese]=passeggeri

        elif anno==prev_anno+1:
            prev_anno=anno
            tot_anni.append(year)
            year=[]
            for i in range(12):
                year.append(0)
            year[mese]=passeggeri
        
    tot_anni.append(year)
    
    #print(tot_anni)    


    
    #CALCOLO DELLE MEDIE
    
    medie=[]
    
    
    num_anni=len(tot_anni)
    d=num_anni-1
    
    for i in range(12):
        c=num_anni-1
        avg=0
        som=0
        
        while c>0:
            #seleziono l'elemento in posizione 'i' della sotto-lista numero 'counter' o 'counter-1' presente nella lista 'tot_anni'
            try:
                primo=int(tot_anni[c][i])
                secondo=int(tot_anni[c-1][i])
            except Exception:
                c=c-1
                d=d-1
                continue

           
            #casi con misurazioni uguali a 0
            if num_anni==2 and (primo==0 or secondo==0):
                avg=0
                break
            
            elif num_anni>2:
                if secondo==0:
                    c=c-1
                    continue
                elif primo==0:
                    d=d-1
                    c=c-1
                    continue
            diff=primo-secondo
            som=som+diff
            c=c-1
                
        #se uno degli anni non è stato reso intero o è 0    
        if num_anni>2 and d<2:
            avg=0
        else:
            avg=som/d
        medie.append(avg)
    

    return medie

    




aa=compute_avg_monthly_difference(time_series, "1949", "1951")
print(aa)