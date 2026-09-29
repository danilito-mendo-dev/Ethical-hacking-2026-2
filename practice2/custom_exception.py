class InvalidGradeError(Exception):
    pass

def verificar_nota(nota):
    if nota < 0 or nota > 10:
        raise InvalidGradeError("La nota debe estar entre 0 y 10")
    return nota

try:
    print(verificar_nota(15))
except InvalidGradeError as e:
    print("Error:", e)