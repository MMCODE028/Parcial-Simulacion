# Creando los Cj del banco


from collections import deque
import random


# Segmento de tiempo 0.5

BoolSimulacion = True

Cj_A = deque()
Cj_B = deque()
Cj_C = deque()
Cj_D = deque()


EsperaTimeA = deque()
EsperaTimeB = deque()
EsperaTimeC = deque()
EsperaTimeD = deque()


# Lista del tamaño de personas

ListaTamaños = [0,0,0,0]

NumeroPersona = 0

# Contadores

Personas_AtendidasA = 0;
Personas_AtendidasB = 0;
Personas_AtendidasC = 0;
Personas_AtendidasD = 0;

TimeTotalA = 0;
TimeTotalB = 0;
TimeTotalC = 0;
TimeTotalD = 0;


TiempoSimulacion = 0

while(BoolSimulacion == True):
    
    AtencionA = random.randint(2,4)
    AtencionB = random.randint(1,3)
    AtencionC = random.randint(3,5)
    AtencionD = random.randint(4,6)

    
    TiempoTotalA = AtencionA + 0.5
    TiempoTotalB = AtencionB + 0.5
    TiempoTotalC = AtencionC + 0.5
    TiempoTotalD = AtencionD + 0.5

    NumeroPersona = NumeroPersona + 1 
    Persona = "Persona " + str(NumeroPersona)

    if(NumeroPersona == 1):
        Cj_A.append(Persona)
        EsperaTimeA.append(TiempoTotalA)
        TimeTotalA = TimeTotalA + TiempoTotalA

    if(NumeroPersona == 2):
        Cj_B.append(Persona)
        EsperaTimeB.append(TiempoTotalA)
        TimeTotalB = TimeTotalB + TiempoTotalB

    if(NumeroPersona == 3):
        Cj_C.append(Persona)
        EsperaTimeC.append(TiempoTotalC)
        TimeTotalC = TimeTotalC + TiempoTotalC

    if(NumeroPersona == 4):
        Cj_D.append(Persona)
        EsperaTimeD.append(TiempoTotalD)
        TimeTotalD = TimeTotalD + TiempoTotalD

    TamañoCJA = len(Cj_A)
    TamañoCJB = len(Cj_B)
    TamañoCJC = len(Cj_C)
    TamañoCJD = len(Cj_D)

    print("Imprimiendo tamaños")

    print("A -->", TamañoCJA)
    print("B -->", TamañoCJB)
    print("C -->", TamañoCJC)
    print("D -->", TamañoCJD)

    # Imprimiendo la lista [Temporar]

    print("Lista Anterior",ListaTamaños)
    
    
    # Vaciamos la lista de tamaños

    ListaTamaños.clear()


    print("Lista Vacia", ListaTamaños)
    


    # Agregamos a la lista los tamaños

    ListaTamaños.append(TamañoCJA)
    ListaTamaños.append(TamañoCJB)
    ListaTamaños.append(TamañoCJC)
    ListaTamaños.append(TamañoCJD)

    print("Lista con elementos Ag", ListaTamaños)


    if(NumeroPersona >= 5):

        # Agregando Persona al menor elemento

        MinimoValor = min(ListaTamaños)
        print("Imprimiendo minimo valor", MinimoValor)

        IndiceDelValor = ListaTamaños.index(MinimoValor)
        print("Imprimiendo indice", IndiceDelValor)        
        
        # Cuando ingresa al banco A 
        if(IndiceDelValor == 0):
            Cj_A.append(Persona)
            TiempoTotalA = random.randint(2,4) + 0.5
            TimeTotalA = TimeTotalA + TiempoTotalA 
            EsperaTimeA.append(TiempoTotalA)
        
        # Cuando ingresa al banco B
        if(IndiceDelValor == 1):
            Cj_B.append(Persona)
            TiempoTotalB = random.randint(1,3) + 0.5
            TimeTotalB = TimeTotalB + TiempoTotalB
            EsperaTimeB.append(TiempoTotalB)

        # Cuando ingresa al banco C
        if(IndiceDelValor == 2):
            Cj_C.append(Persona)
            TiempoTotalC = random.randint(3,5) + 0.5
            TimeTotalC = TimeTotalC + TiempoTotalC
            EsperaTimeC.append(TiempoTotalC)

        # Cuando ingresa al banco D  
        if(IndiceDelValor == 3):
            Cj_D.append(Persona)
            TiempoTotalD = random.randint(4,6) + 0.5
            TimeTotalD = TimeTotalD + TiempoTotalD 
            EsperaTimeD.append(TiempoTotalD)

        print("-----------------------------------------------------------------")

        print("Imprimiendo Diferentes colas [Personas]")
        
        print("Imprimiendo Personas A ---> ", Cj_A)
        print("Imprimiendo Personas B ---> ", Cj_B)
        print("Imprimiendo Personas C ---> ", Cj_C)
        print("Imprimiendo Personas D ---> ", Cj_D)


        print("Imprimiendo Diferentes colas [Tiempo]")

        print("Imprimiendo cola A ---> ", EsperaTimeA)
        print("Imprimiendo cola B ---> ", EsperaTimeB)
        print("Imprimiendo cola C ---> ", EsperaTimeC)
        print("Imprimiendo cola D ---> ", EsperaTimeD)

        # Restando 0.5 Minutos a cada cola

        print("Obteniendo el primer valor",EsperaTimeA[0])
        EliminacionA = EsperaTimeA[0] - 0.5
        print("Restando el primero Valor ",EliminacionA )
        EsperaTimeA.popleft()
        print("Agregamos el elemento actualizado", EsperaTimeA.insert(0,EliminacionA))
        print("Obteniendo el primer valor actualizador", EsperaTimeA[0])     


        
        print("Obteniendo el primer valor",EsperaTimeA[0])
        EliminacionB = EsperaTimeB[0] - 0.5
        print("Restando el primero Valor ",EliminacionA )
        EsperaTimeB.popleft()
        print("Agregamos el elemento actualizado", EsperaTimeB.insert(0,EliminacionB))
        print("Obteniendo el primer valor actualizador", EsperaTimeB[0])     

        
        print("Obteniendo el primer valor",EsperaTimeC[0])
        EliminacionC = EsperaTimeC[0] - 0.5
        print("Restando el primero Valor ",EliminacionB )
        EsperaTimeC.popleft()
        print("Agregamos el elemento actualizado", EsperaTimeC.insert(0,EliminacionC))
        print("Obteniendo el primer valor actualizador", EsperaTimeC[0])     

        
        print("Obteniendo el primer valor",EsperaTimeD[0])
        EliminacionD = EsperaTimeD[0] - 0.5
        print("Restando el primero Valor ",EliminacionD )
        EsperaTimeD.popleft()
        print("Agregamos el elemento actualizado", EsperaTimeD.insert(0,EliminacionD))
        print("Obteniendo el primer valor actualizador", EsperaTimeD[0])     

        if(EsperaTimeA[0] == 0):
            EsperaTimeA.popleft()
            Cj_A.popleft()
            Personas_AtendidasA = Personas_AtendidasA + 1;


        if(EsperaTimeB[0] == 0):
            EsperaTimeB.popleft()
            Cj_B.popleft()
            Personas_AtendidasB = Personas_AtendidasB + 1;

        if(EsperaTimeC[0] == 0):
            EsperaTimeC.popleft()
            Cj_C.popleft()
            Personas_AtendidasC = Personas_AtendidasC + 1;

        if(EsperaTimeD[0] == 0):
            EsperaTimeD.popleft()
            Cj_D.popleft()
            Personas_AtendidasD = Personas_AtendidasD + 1;



            


    # print("Imprimiendo listas del personas ")

    # print("Cajero A ->", Cj_A)
    # print("Cajero B ->", Cj_B)
    # print("Cajero C ->", Cj_C)
    # print("Cajero D ->", Cj_D)

    # print("Imprimiendo numeros aleatorios ")

    # print("Tiempo de Atencion A ", EsperaTimeA)
    # print("Tiempo de Atencion B ", EsperaTimeB)
    # print("Tiempo de Atencion C ", EsperaTimeC)
    # print("Tiempo de Atencion D ", EsperaTimeD)


    TiempoSimulacion = TiempoSimulacion + 0.5

    if(TiempoSimulacion == 480):
        BoolSimulacion = False
        break;

    # --------------------------------------------------------------------------------
    # respuesta = str(input("Quiere seguir con la simulacion? y/n "))
    
    
    # if(respuesta == 'y'):
    #     BoolSimulacion == False
    # else:
    #     break


print("Personas Atendidas Cajero A ---> ", Personas_AtendidasA )
PSinAtenderA = len(EsperaTimeA) 
PSinAtenderB=len(EsperaTimeB)
PSinAtenderC=len(EsperaTimeC) 
PSinAtenderD=len(EsperaTimeD)
print("Personas Atendidas Cajero B ---> ", Personas_AtendidasB )
print("Personas Atendidas Cajero C ---> ", Personas_AtendidasC )
print("Personas Atendidas Cajero D ---> ", Personas_AtendidasD )
Total = Personas_AtendidasA + Personas_AtendidasB + Personas_AtendidasC + Personas_AtendidasD
print("Total de personas atentidas BANCO 1", Total)
print("Tiempo de simulacion", TiempoSimulacion)
print("Tiempo Total A -->", TimeTotalA)
print("Tiempo Promedio Para A ->", TimeTotalA / (Personas_AtendidasA + PSinAtenderA))
print("Tiempo Promedio Para B ->", TimeTotalB / (Personas_AtendidasB + PSinAtenderB))
print("Tiempo Promedio Para C ->", TimeTotalC / (Personas_AtendidasC + PSinAtenderC))
print("Tiempo Promedio Para D ->", TimeTotalD / (Personas_AtendidasD + PSinAtenderD))