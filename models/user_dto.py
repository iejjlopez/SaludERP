from dataclasses import dataclass

@dataclass
class UserDTO:
    username: str
    role: str
    is_active: bool = True