def sum_csv(file_name):
    values = []
    fun = open(file_name, 'r')
    for line in fun:
        elements = line.split(',')
        if elements[0] != 'Date':
            #date = elements[0]
            value = elements[1]
            try:
                values.append(float(value))
            except ValueError:
                values.append(0)
        
    if len(values) == 0:
        return None
    else:
        somma = sum(values)

    return somma




