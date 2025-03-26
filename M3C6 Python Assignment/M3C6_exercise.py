# Crear una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 

class Usuario:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return f"Usuario: {self.user_name}"

# Crear un objeto usando la clase
user = Usuario("Lorena", "Bilbao25*")

print(f"Hola {user.user_name}, tu contraseña es {user.password}")