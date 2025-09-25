import math

def relaciofugg(szam1:int,szam2:int):
    eredmeny=""
    if szam1>szam2:
        eredmeny= ">"
    elif szam1<szam2:
        eredmeny="<"
    else:
        eredmeny="="
    return eredmeny

def relaciokiiras():
    print(relaciofugg())

def kerulet(sugar):
    if sugar<0:
        print("hiba: A kör sugara nem pozitív!")
    else:
        return 2*sugar*3.14

def terulet(sugar):
    if sugar<0:
        print("hiba: A kör sugara nem pozitív!")
    return sugar**2*3.14

def korkiiras(sugar):
    print(f"A kör kerülete: {kerulet(sugar)}")
    print(f"A kör területe: {terulet(sugar)}")