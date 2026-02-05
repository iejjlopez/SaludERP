from models.user_dto import UserDTO

class AuthService:
    @staticmethod
    def validate_user(username, password):
        # Limpieza de datos para evitar "Credenciales inválidas" accidentales
        clean_user = username.strip().upper()
        
        # Validación con las credenciales que usaste en la captura
        if clean_user == "ADMINGENERAL" and password == "admin123":
            return UserDTO(username=clean_user, role="Administración")
        
        return None