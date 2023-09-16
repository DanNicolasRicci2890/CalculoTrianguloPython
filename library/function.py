from tkinter import messagebox as MessageBox

def NombreTriangulo(txl, txa):
    stg = ""
    if (txl == 1):
        stg = "Equilatero"
    elif (txl == 2):
        stg = "Isosceles - "        
    elif (txl == 3):
        stg = "Escaleo - "
    if (txl != 1):
        if (txa == 1):
            stg += "Acutangulo"
        elif (txa == 2):
            stg += "Rectangulo"
        elif (txa == 3):
            stg += "Obtusangulo"
    return stg    

def VerificarContenido(list):
    k = False
    if ((list[0] == 4) and (list[1] == 4) and (list[2] == 4)):
        k = True
    else:
        sty = "Verificar los campos:\n"
        for i in range(3):
            if (list[i] != 4):
                if (i == 0):
                    sty += " lado A: "
                if (i == 1):
                    sty += " lado B: "                    
                if (i == 2):
                    sty += " lado C: "                    
                if ((list[i]) == 0):
                    sty += " Completar el Campo. \n"
                if ((list[i]) == 1):
                    sty += " Solamente numeros, no letras u otros caracteres. \n"  
                if ((list[i]) == 2):
                    sty += " numeros positivos, no se aceptan numeros negativos. \n"                 
                if ((list[i]) == 3):
                    sty += " no se acepta el numero cero, solo numeros positivos. \n"                                               
        MessageBox.showwarning("Alerta", sty)            
    return k