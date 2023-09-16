from headermain import *

def CalcularTriangulo():
    triang = Triangulo(nA.get(), nB.get(), nC.get())
    verif = triang.VerifValueLado()
    
    if (VerificarContenido(verif)): # verifica el contenido de los lados
        
        if (triang.VerifTriangulo()): # verifica si los tres lados son un triangulo
            
            triang.CalificarTrianguloxLado() # Califica si es Equilatero, Isosceles o Escaleno
            triang.CalcularAngulos() # Calculamos los Angulos del triangulo
            triang.CalibrarAngulos() # Calibramos los Angulos del triangulo
            triang.CalificarTrianguloxAngulo() # Calificamos si es Acutangulo, Rectangulo o Obtusangulo            
            triang.CalcularPerimetro() # Calculamos el perimetro
            triang.CalcularSuperficie() # Calculamos la Superficie
                                 
            stg = NombreTriangulo(triang.getTriangLado(),triang.getTriangAng())                        
            label_typetrian.config(text=str(stg))
            stg = " Alfa° = " + str(triang.getAlfa()) + "°"
            label_AngAlfa.config(text=stg)
            stg = " Beta° = " + str(triang.getBeta()) + "°"
            label_AngBeta.config(text=stg)
            stg = "Gamma° = " + str(triang.getGamma()) + "°"
            label_AngGamma.config(text=stg)
            
            stg = " perimetro = " + str(triang.getPerimetros()) + " u"
            label_Perimetro.config(text=stg)
            stg = "superficie = " + str(triang.getSuperficie()) + " u2"
            label_Superficie.config(text=stg)    
            resp1 = MessageBox.askquestion("Consulta"," ¿ desea volver a calcular devuelta ? ")      
            if (resp1 == "yes"):
                LimpiarNuevo()
            elif (resp1 == "no"):
                resp2 = MessageBox.askquestion("Consulta"," ¿ desea salir del programa ? ")                      
                if (resp2 == "yes"):
                    Salir()
        else:
            MessageBox.showinfo("Aviso!", "Los lados ingresados\nno Forman un triangulo")
            LimpiarNuevo()
    else:
        LimpiarNuevo()

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

def LimpiarNuevo():
    nA.set("")
    nB.set("")
    nC.set("")
    label_typetrian.config(text="")
    label_AngBeta.config(text="")
    label_AngAlfa.config(text="")
    label_AngGamma.config(text="")
    label_Perimetro.config(text="")
    label_Superficie.config(text="")
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

def Salir():
    root.destroy()
   
root = Tk()

nA = StringVar()
nB = StringVar()
nC = StringVar()


ventanaroot(root) # crear la ventada interactiva

btn_Aceptar = Button(root, text=" ACEPTAR ", command=CalcularTriangulo)
btn_Nuevo = Button(root, text="  NUEVO  ", command=LimpiarNuevo)
btn_Salir = Button(root, text="    SALIR    ", command=Salir)

# crear los textobox de ingreso de lados del triangulo
CrearTextBox(root, "Lado A: ", nA, 300, 50, 10, 20)
CrearTextBox(root, "Lado B: ", nB, 300, 50, 10, 90)
CrearTextBox(root, "Lado C: ", nC, 300, 50, 10, 160)

label_typetrian = Label(root)
label_typetrian.config(font=("Verdana", 16, "bold", "italic"), background="#BEBFB2", foreground="blue")
label_typetrian.place(x=500, y=20)

label_AngAlfa = Label(root)
label_AngAlfa.config(font=("Verdana", 16, "italic"), background="#BEBFB2", foreground="green")
label_AngAlfa.place(x=410, y=70)

label_AngBeta = Label(root)
label_AngBeta.config(font=("Verdana", 16, "italic"), background="#BEBFB2", foreground="green")
label_AngBeta.place(x=400, y=120)

label_AngGamma = Label(root)
label_AngGamma.config(font=("Verdana", 16, "italic"), background="#BEBFB2", foreground="green")
label_AngGamma.place(x=370, y=170)

label_Perimetro = Label(root)
label_Perimetro.config(font=("Verdana", 16, "italic"), background="#BEBFB2", foreground="blue")
label_Perimetro.place(x=600, y=70)

label_Superficie = Label(root)
label_Superficie.config(font=("Verdana", 16, "italic"), background="#BEBFB2", foreground="blue")
label_Superficie.place(x=607, y=110)

btn_Aceptar.config(font=("Console", 16, "bold"))
btn_Nuevo.config(font=("Console", 16, "bold"))
btn_Salir.config(font=("Console", 16, "bold"))
btn_Aceptar.place(width=130, height=50, x=10, y=230)
btn_Nuevo.place(width=130, height=50, x=180, y=230)
btn_Salir.place(width=300, height=50, x=10, y=300)
root.mainloop()
