#/-----MÁXIMO COMÚN DIVISOR-----/

def mcd(a, b):
  
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
    
    mcd(a, b)  
           
    sim1 = str(int(a/mcd(a, b)))
    sim2 = str(int(b/mcd(a, b)))
    
    if sim2 == 1:
        return sim1
    else:
        return sim1 +'/'+ sim2

    
#/-----SUMA DE FRACCIONES-----/

def suma(a,a2,b,b2):    
    
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

def mult(a,a2,b,b2):   
    
    while a2!=0 and b2!=0:

        numMult = str(int(a*b))
        denMult = str(int(a2*b2))

        return numMult +'/'+ denMult
    
    return 'ERROR'


#/-----DIVISIÓN DE FRACCIONES-----/

def div(a,a2,b,b2):
    
    while a2!=0 and b2!=0:
        
        numDiv = str(int(a*b2))
        denDiv = str(int(b*a2))

        return numDiv +'/'+ denDiv
    
    return 'ERROR'