class Model():
    def fit(self, data):
# Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    
    def predict(self, data):
# Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        self.average_diff=0
        prev_value = None
        diff_tot = 0
        n = 0
        for item in data:

            if (prev_value == None):
                prev_value = item

            else:
                diff = item - prev_value
                prev_value = item
                diff_tot = diff_tot + diff
                n = n + 1

        
        
        try:
            self.average_diff = diff_tot / n

        except ZeroDivisionError as e:
            print('Non ho potuto calcolare la media a causa di questo errore: {}' .format(e))
            
            
        prediction = prev_value + self.average_diff
        
        return prediction