import math

class Triangulo:
    _LadoA = ""
    _LadoB = ""
    _LadoC = ""
    _Alfa = 0.0
    _Beta = 0.0
    _Gamma = 0.0
    _typetrian = 0
    _typedeegre = 0
    _Perimetro = 0.0
    _Superficie = 0.0
    
    # Constructor
    def __init__(self, nA, nB, nC):
        self._LadoA = nA
        self._LadoB = nB
        self._LadoC = nC
        self._Alfa = 0.0
        self._Beta = 0.0
        self._Gamma = 0.0
        self._typetrian = 0        
        self._typedeegre = 0
        self._Perimetro = 0.0
        self._Superficie = 0.0
        
    # Calcular la Superficie
    def CalcularSuperficie(self):
        base = 0
        altura = 0
        if (self._typetrian == 1):
            base = float(self._LadoA)
            altura = float(self._LadoA) / (math.sin(math.radians(self._Alfa)))
            
        elif (self._typetrian == 2):
            if (self._typedeegre == 2):
                if (float(self._LadoA) == float(self._LadoB)):
                    base = altura = float(self._LadoA)
                elif (float(self._LadoB) == float(self._LadoC)):
                    base = altura = float(self._LadoB)
                elif (float(self._LadoC) == float(self._LadoA)):
                    base = altura = float(self._LadoC)
            else:
                if (float(self._LadoA) == float(self._LadoB)):
                    base = float(self._LadoC)
                    altura = float(self._LadoA) / (math.sin(math.radians(self._Alfa)))
                elif (float(self._LadoB) == float(self._LadoC)):
                    base = float(self._LadoA)
                    altura = float(self._LadoB) / (math.sin(math.radians(self._Beta)))
                elif (float(self._LadoC) == float(self._LadoA)):
                    base = float(self._LadoB)
                    altura = float(self._LadoC) / (math.sin(math.radians(self._Gamma)))
                    
        elif (self._typetrian == 3):
            lk = [ float(self._LadoA) , float(self._LadoB) , float(self._LadoC) ]
            lq = [ self._Alfa , self._Beta , self._Gamma ]
            lk.sort()                                                 
            lq.sort()                                   
            if (self._typedeegre == 2):
                base = lk[1]
                altura = lk[0]
            else:
                base = lk[2]
                altura = lk[1] / math.sin(math.radians(lq[2]))
        self._Superficie = round((base * altura) / 2)
    
    # Calcular el Perimetro
    def CalcularPerimetro(self):
        self._Perimetro = (float(self._LadoA)) + (float(self._LadoB)) + (float(self._LadoC))
        
    # Calificar Triangulo x Angulo
    def CalificarTrianguloxAngulo(self):
        if (self._typetrian == 1):
            self._typedeegre = 1
        else:
            lk = [ self._Alfa , self._Beta , self._Gamma ]    
            self._typedeegre = 1 # angulo Acutangulo
            i = 0
            while((i < 3) and (self._typedeegre == 1)):
                if (lk[i] == 90):
                    self._typedeegre = 2 # angulo Rectangulo
                elif (lk[i] >= 92):
                    self._typedeegre = 3 # angulo Obtusangulo
                i+=1        
            if ((self._typetrian == 2) and (self._typedeegre == 2)):
                i = 0
                while(i < 3):
                    if (lk[i] != 90):
                        lk[i] = 45
                    i+=1
                self._Alfa = lk[0]
                self._Beta = lk[1]
                self._Gamma = lk[2]
    
    # Calibrar los Angulos del triangulo
    def CalibrarAngulos(self):
        alfa = 0
        beta = 0
        gama = 0        
        if (self._typetrian != 1):
            if (self._Alfa <= 92) and (self._Alfa >= 88):
                alfa = 90
                beta = round(self._Beta, 1) + 1
                gama = round(180 - (alfa + beta))
            if (self._Beta <= 92) and (self._Beta >= 88):    
                beta = 90
                gama = round(self._Gamma, 1) + 1
                alfa = round(180 - (gama + beta))
            if (self._Gamma <= 92) and (self._Gamma >= 88):    
                gama = 90
                alfa = round(self._Alfa, 1) + 1
                beta = round(180 - (gama + alfa), 1)
        if (alfa != 0):
            self._Alfa = alfa
        else:
            self._Alfa = round(self._Alfa, 1)
        if (beta != 0):
            self._Beta = beta     
        else:
            self._Beta = round(self._Beta, 1)
        if (gama != 0):
            self._Gamma = gama
        else:
            self._Gamma = round(self._Gamma, 1)
        
    # Calcular los Angulos del triangulo
    def CalcularAngulos(self):
        if (self._typetrian == 1):
            # si el triangulo es equilatero por definicion
            # es acutangulo y sus angulos miden 60°
            self._Alfa = 60
            self._Beta = 60
            self._Gamma = 60
        else:
            self._Alfa = self.__DegreeAlfa__()
            self._Beta = self.__DegreeBeta__()
            self._Gamma = self.__DegreeGamma__()
            
    # Calificar un triangulo (Equilatero, Isosceles, Escaleno)
    def CalificarTrianguloxLado(self):
        self._typetrian = 2
        a = float(self._LadoA)
        b = float(self._LadoB)
        c = float(self._LadoC)
        if ((a == b) and (b == c)):
            self._typetrian = 1
        elif ((a != b) and (b != c) and (c != a)):
            self._typetrian = 3

    
    # Verificar si los valores numeros conforman un triangulo
    def VerifTriangulo(self):
        h = False
        a = float(self._LadoA)
        b = float(self._LadoB)
        c = float(self._LadoC)        
        if (a < (b + c)):
            if (b < (a + c)):
                if (c < (a + b)):
                    h = True
        return h
           
    # Verifica si el valor de los lados son correctos    
    def VerifValueLado(self):
        List_V = []
        List_V.append(Triangulo.VerifVLad(self._LadoA))
        List_V.append(Triangulo.VerifVLad(self._LadoB))
        List_V.append(Triangulo.VerifVLad(self._LadoC))
        return List_V
                    
    def getAlfa(self):
        return (self._Alfa)                    

    def getBeta(self):
        return (self._Beta)      
    
    def getGamma(self):
        return (self._Gamma)  
    
    def getTriangLado(self):
        return (self._typetrian)  

    def getTriangAng(self):
        return (self._typedeegre)

    def getPerimetros(self):
        return (self._Perimetro)
    
    def getSuperficie(self):
        return (self._Superficie)                                       
    
    def VerifVLad(num):
        STAT = 0
        if (len(num) > 0): # verificar si el valor ingresado es distinto del null            
            # verificar si es un numero
            try:
                val = float(num)    
                STAT = 2 
                # verificar si el numero es positivo
                if (val >= 0):
                    STAT = 3 # verificar si el distinto del numero cero
                    if (val > 0):
                        STAT = 4 # numero correcto                     
            except:                            
                STAT = 1                                       
        return STAT        
    
    # alfa = arcos((a2 - (b2 + c2)) / -2bc)
    def __DegreeAlfa__(self):
        a = float(self._LadoA)
        b = float(self._LadoB)
        c = float(self._LadoC)
        gc = ((math.pow(a, 2)) - ((math.pow(b, 2)) + (math.pow(c, 2)))) / (-2*b*c)
        alfa = math.degrees(math.acos(gc))
        return alfa
    
    # beta = arcsin((b/a)*sin(alfa))
    def __DegreeBeta__(self):
        a = float(self._LadoA)
        b = float(self._LadoB)        
        gc = ((b/a)*(math.sin(math.radians(self._Alfa))))    
        beta = math.degrees(math.asin(gc))
        return beta
    
    # gamma = 180 - (alfa + beta)
    def __DegreeGamma__(self):
        gamma = 180 - (self._Alfa + self._Beta)
        return gamma

    
    