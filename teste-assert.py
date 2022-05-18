## Assert é uma especificação onde dizemos a forma de como deve se comportar o código

# Exemplo de assert

def testanumeros(a,b):
    assert a > 0 and b > 0, "Números precisam ser maiores do que zero"
    return a+b
    
print(testanumeros(0,3))

