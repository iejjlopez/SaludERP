from models.user_dto import UserDTO

class AuthService:
    @staticmethod
    def validate_user(username, password):
        # Limpieza para asegurar compatibilidad en la nube
        clean_user = username.strip().upper()
        
        if clean_user == "ADMINGENERAL" and password == "admin123":
            return UserDTO(username=clean_user, role="Administración")
        
        return None