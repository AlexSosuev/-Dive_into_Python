class User:
    def __init__(self, name: str, u_id: str, level: int = 0):
        self.name = name
        self.u_id = u_id
        self.level = level

    def __eq__(self, other):
        if isinstance(other, User):
            if self.name == other.name and self.u_id == other.u_id:
                return True
            else:
                return False

    def __hash__(self):
        return hash(self.name + self.u_id)
    def __str__(self):
        return f'{self.name ({self.u_id}): Уровень доступа {self.level}}'
    
    def __repr__(self):
        return f'{self.name ({self.u_id}): Уровень доступа {self.level}}'