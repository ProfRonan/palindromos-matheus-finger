"""Main functions"""

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    texto = string.lower()
    for i in range(0, len(texto)):
        if not texto[i].isalnum():
            if i == 0:
                if len(texto) != 1:
                    texto = " " + texto[1:]
                else:
                    return False
            elif i == len(texto)-1:
                texto = texto[:i] + " "
            else:
                texto = texto[:i] + " " + texto[i+1:]
    texto = texto.replace(" ", "")
    teste = ''
    for i in range(len(texto)-1, -1 ,-1):
        teste = teste + texto[i]
    if teste == texto:
        return True
    else:
        return False