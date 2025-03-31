class Login:
    def __init__(self):
        self.archivo = 'Usuarios.txt'
        
    def obtener_usuarios(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return [linea.strip().split(':') for linea in f if linea.strip()]
        except FileNotFoundError:
            return []
        
    def registrar_usuarios(self, usuario, password):
        with open(self.archivo, 'a', encoding='utf-8') as f:
            f.write(f'{usuario}:{password}\n')
            
    def iniciar_sesion(self):  
        print("Bienvenido al sistema ".center(50, "="))
        usuario = input("Por favor ingrese su usuario: ")
        password = input("Por favor ingrese su contraseña: ")
    
        for u, p in self.obtener_usuarios():  
            if u == usuario and p == password:
                print(f"\n¡Bienvenido {usuario}!")
                return True
        print("\nUsuario o contraseña incorrectos. Intente de nuevo.")
        return False
    
    def validar_usuario(self, usuario):
        """Valida que el usuario solo contenga letras"""
        return usuario.isalpha()
    
    def validar_password(self, password):
        """Valida que la contraseña solo contenga números"""
        return password.isdigit()
    
    def registrar(self):
        print("Bienvenido al sistema de registro".center(50, "="))
        while True:
            
            usuario = input("Por favor ingrese un usuario (solo letras): ")
            if not usuario: 
                print("Error: El usuario no puede estar vacío.")
                continue
            if not self.validar_usuario(usuario):
                print("Error: El usuario solo debe contener letras (a-z, A-Z).")
                continue
            
            
            password = input("Por favor ingrese una contraseña (solo números): ")
            if len(password) < 6:
                print("Error: La contraseña debe tener al menos 6 dígitos.")
                continue
            if not self.validar_password(password):
                print("Error: La contraseña solo debe contener números (0-9).")
                continue
            
            
            if any(u[0] == usuario for u in self.obtener_usuarios()):  
                print("Error: El usuario ya existe.")
                continue  
            
           
            self.registrar_usuarios(usuario, password)
            print("\n¡Registro exitoso! Ahora puede iniciar sesión.")
            break
    
def mostrar_menu():
    print("\n" + "="*40)
    print(" Sistema Usuarios - Bienvenido ".center(40))
    print("="*40)
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    print("="*40)
    
if __name__ == "__main__":
    sistema = Login()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == '1':
            sistema.iniciar_sesion()  
        elif opcion == '2':
            sistema.registrar()
        elif opcion == '3':
            print("\nSesión finalizada")
            break
        else:
            print("Opción no válida")
        
        input("\nPresione Enter para continuar...")