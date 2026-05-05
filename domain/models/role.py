from typing import Optional


class Role:

    def __init__(self, role_id: Optional[int], name: str, level: str):
        self.id = role_id
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.id} - {self.name} ({self.level})"
