from models.user_dto import UserDTO

class AuthService:
    @staticmethod
    def login(username, password):
        # Limpieza de datos para evitar "Credenciales inválidas" accidentales
        clean_user = username.strip().upper()
        
        if clean_user == "ADMINGENERAL" and password == "admin123":
            return UserDTO(username=clean_user, role="Administración")
        
        return None