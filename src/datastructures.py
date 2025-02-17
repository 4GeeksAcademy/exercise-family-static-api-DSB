class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generate_id(self):
        """Genera un ID único para cada miembro."""
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        """Agrega un nuevo miembro con un ID único."""
        if "id" not in member or member["id"] is None:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        """Elimina un miembro por ID."""
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        """Obtiene un miembro por ID."""
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        """Devuelve todos los miembros de la familia."""
        return self._members
