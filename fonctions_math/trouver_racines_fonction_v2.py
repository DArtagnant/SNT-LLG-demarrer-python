
class tousReels(Exception): pass
class aucunsReels(Exception): pass



def find(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return tousReels()
            else:
                return aucunsReels()
        else:
            return -c/b
    else:
        d = (b**2)-(4*a*c)
        if d > 0:
            return ((-b+(d**0.5))/(2*a), (-b-(d**0.5))/(2*a))
        elif d == 0:
            return (-b)/(2*a)
        else:
            return aucunsReels()

def from_string(string: str):
    #on enleve les caracteres inutiles
    string = string.replace(" ", "").replace("x", "").replace("*", "").replace("²", "")
    #si il y a un -, on garde +- 
    string = string.replace("+-", "-")

    return string


if __name__ == "__main__":
    print(from_string(input("t: ")))
    
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))

