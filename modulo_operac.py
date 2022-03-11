#/-----MÁXIMO COMÚN DIVISOR-----/

def mcd(a, b):
  
  """Función que calcula el MCD de dos enteros y los convierte a fracción"""
  
    if a > b:
        peq = b
    else:
        peq = a
        
    for i in range(1, peq+1):
        if((a % i == 0) and (b % i == 0)):
            mcd = i
            
    return mcd


#/-----SIMPLIFICACIÓN DE FRACCIONES-----/

def simplif(a, b):
    """Función que simplifica una fracción"""
    
    mcd(a, b)  
           
    sim1 = str(int(a/mcd(a, b)))
    sim2 = str(int(b/mcd(a, b)))
    
    if sim2 == 1:
        return sim1
    else:
        return sim1 +'/'+ sim2

    
#/-----SUMA DE FRACCIONES-----/

def suma(a,a2,b,b2):    
    """Función que calcula la suma entre dos fracciones"""

    
    while a2!=0 and b2!=0:
        
        if a2 != b2:
            numSuma = str(int(a*b2+a2*b))
            denSuma = str(int(a2*b2))
        else:
            numSuma = str(int(a+b))
            denSuma = str(int(a2))        
        return numSuma +'/'+ denSuma
    
    return 'ERROR'


#/-----RESTA DE FRACCIONES-----/
    """Función que calcula la resta entre dos fracciones"""

def resta(a,a2,b,b2):    
    
    while a2!=0 and b2!=0:
        
        if a2 != b2:
            numResta = str(int(a*b2-a2*b))
            denResta = str(int(a2*b2))
        else:
            numResta = str(int(a-b))
            denResta = str(int(a2))        
        return numResta +'/'+ denResta
    
    return 'ERROR'


#/-----MULTIPLICACIÓN DE FRACCIONES-----/
    """Función que calcula la multiplicación entre dos fracciones"""

def mult(a,a2,b,b2):   
    
    while a2!=0 and b2!=0:

        numMult = str(int(a*b))
        denMult = str(int(a2*b2))

        return numMult +'/'+ denMult
    
    return 'ERROR'


#/-----DIVISIÓN DE FRACCIONES-----/
    """Función que calcula la división entre dos fracciones"""


def div(a,a2,b,b2):
    
    while a2!=0 and b2!=0:
        
        numDiv = str(int(a*b2))
        denDiv = str(int(b*a2))

        return numDiv +'/'+ denDiv
    
    return 'ERROR'
