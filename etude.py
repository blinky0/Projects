from sympy import *
import re 


x=symbols('x')
fonction=input("")

fonction =sympify(fonction)


domaine=str((calculus.util.continuous_domain(fonction,x,S.Reals)))

valeurs=re.findall(r'[-+]?\d*\.?\d+(?:/\d*\.?\d+)?',domaine)

def limitinf(fonction):
    limpinf=limit(fonction,x,oo)
    return limpinf

def limitneginf(fonction):
    lim_ninf=limit(fonction,x,-oo)
    return lim_ninf

def limite(fonction,z,a):
    lim=limit(fonction,x,z,a)
    if "I" in str(lim):
        pass
    else:
        return lim

def limitesdedf(fonction):
    if "oo" in domaine or domaine=="Reals":
        print(limitinf(fonction))
    if "-oo" in domaine or domaine=="Reals": 
        print(limitneginf(fonction))
    for i in valeurs:
        if valeurs.count(i)>1: #les valeurs de separation(repetitives)
            print(limite(fonction,int(i),'+'),limite(fonction,int(i),'-'))
            break
        else: 
            print(limite(fonction,int(i),'+'),limite(fonction,int(i),'-')) #doit trouver un moyen de diviser qd xo- est pas dans lintervalle

limitesdedf(fonction)
print(domaine)

#on passe a la derivabilite
#Puisque f est continue alors limage dun point c sa limite 

def derivabilite(nombre):
    image=limit(fonction,x,int(nombre))
    if "oo" in str(image):
        pass
    else:
        image=image
        print(image)
        derivee=limit((fonction-image)/(x-nombre),x,nombre)
        if "I" in str(derivee):
            derivee="-oo"
            return derivee
        return derivee 

def monotonie(fonction,intervalle):
    croissante=is_increasing(fonction,intervalle)
    decroissante=is_decreasing(fonction,intervalle)
    if croissante==True:
        return "elle est croissante sur cet inrerval"
    if decroissante==True:
        return "elle est decroissante sur cet intervalle"



def derivation(fonction):
    derive=diff(fonction) 
    print(derive)
    solution=solveset(derive,x,domain=calculus.util.continuous_domain(fonction,x,S.Reals))
    print(solution)
    monotone=is_monotonic(fonction,interval=calculus.util.continuous_domain(fonction,x,S.Reals))
    print(monotone)
    if monotone==True:
        print(monotonie(fonction,calculus.util.continuous_domain(fonction,x,S.Reals)))
    elif monotone==False:
        for i in solution:
            intervale=str(Interval(i,i).symmetric_difference(calculus.util.continuous_domain(fonction,x,S.Reals)))
            i_1=intervale.replace("Union(","", 1)
            print(intervale)
            i_1=re.split(r"\),",i_1,1 )

            i_f1=i_1[0]+")"
            i_3=i_1[1]
            print(i_f1)
            i_f2=i_3[:-1].replace(" ","",1)
            print(i_f2)
            print(monotonie(fonction,sympify(i_f1)),i_f1)
            print(monotonie(fonction,sympify(i_f2)),i_f2)
       
derivation(fonction)




