def kisebbnagyobbrelacio():
    a = int(input("Kérem az első számot: "))
    b = int(input("Kérem a második számot: "))
    e = ""
    if a < b:
        e = "<"
    elif a > b:
        e = ">"
    else:
        e = "="
    return e

def relacio(a, b, e):
    a = int(input("Kérem az első számot: "))
    b = int(input("Kérem a második számot: "))
    e = str(input("Kérem a relációs jelet (<, >, =): "))
    if a < b and (e == "<" or e == ">"):
        print(f'{a} < {b}')
    elif a > b and (e == ">" or e == "<"):
        print(f'{a} > {b}')
    elif a == b and e == "=":
        print(f'{a} = {b}')
    else:
        print("Hibás relációs jel!")

relacio(3, 5, "<")