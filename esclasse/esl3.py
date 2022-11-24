def sum_csv(my_file):

    values = []
    somma = 0

    file = open('my_file', 'r')
    for line in my_file:
        elements = line.split(',')

        if elements[0] != 'Date' :

            value = elements[1]

            values.append(value)

    for value in values:
        somma = somma + value

    return somma
