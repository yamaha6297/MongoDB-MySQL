from datetime import date, timedelta

def avg (array):
    timeInitial = timedelta(0,0,0)
    for i in array:
        timeInitial += i
    return (timeInitial/len(array))
