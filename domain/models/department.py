from typing import Optional


class Department:

    def __init__(self, department_id: Optional[int], name: str):
        self.id = department_id
        self.name = name
    
    def __str__(self):
        return f"{self.id} - {self.name}"
