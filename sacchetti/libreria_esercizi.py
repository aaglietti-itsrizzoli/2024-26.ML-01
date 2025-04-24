import math

def E1_Triangoli_ask():
    tmp = 0
    lati = []
    for i in range (3):
        while (tmp <= 0):
            try:
                tmp = int(input("Inserisci un lato del triangolo, (numero intero maggiore di Zero): "))
            except:
                print("Errore: tipo non valido")
            lati.append(tmp)
        tmp = -1
    return lati

def E1_Triangoli_classifier(lati):
    tmp = -1
    if ((lati[0] + lati[1] <= lati[2]) or (lati[0] + lati[2] <= lati[1]) or (lati[2] + lati[1] <= lati[0])):
        print("Il triangolo non si può formare")
        return "N/A"
    else:
        if (lati[0] == lati [1] == lati[2]):
            print("Il triangolo è equilatero")
            return "EQUILATERO"
        elif ((lati[0] == lati [1]) or (lati[0] == lati [2]) or (lati[2] == lati [1])):
            print("Il triangolo è isoscele")
            return "ISOSCELE"
        else:
            print("Il triangolo è scaleno")
            return "SCALENO"

def E1_Triangoli_perimetro(lati):
        if E1_Triangoli_isValidTriangolo(lati[0], lati[1], lati[2]):
            perimetro = lati[0] + lati[1] + lati[2]
            return perimetro
        else:
            raise ValueError("Il triangolo non è valido, non è possibile calcolare il perimetro.")

def E1_Triangoli_area(lati):
        pmezzi = E1_Triangoli_perimetro(lati) / 2
        area = math.sqrt(pmezzi*(pmezzi - lati[0])*(pmezzi - lati[1])*(pmezzi - lati[2]))
        return round(area, 2)

def E1_Triangoli_isValidTriangolo(lato1, lato2, lato3):
    if (lato1 + lato2 > lato3) and (lato1 + lato3 > lato2) and (lato2 + lato3 > lato1):
        return True
    else:
        return False
    
def E3_ListaStringa(lista):
    stringa = ''.join(e + "_" for e in lista)[:-1]
    return stringa