class Galaxia:
    def __init__(self, _id, name, type, distance_ly, num_stars, num_planets):
        self._id = _id
        self.name = name
        self.type = type
        self.distance_ly = distance_ly
        self.num_stars = num_stars
        self.num_planets = num_planets

class SistemaSolar:
    def __init__(self, _id, name, galaxia_id):
        self._id = _id
        self.name = name
        self.galaxia_id = galaxia_id

class Estrella:
    def __init__(self, _id, name, sistema_solar_id):
        self._id = _id
        self.name = name
        self.sistema_solar_id = sistema_solar_id

class Planeta:
    def __init__(self, _id, name, sistema_solar_id):
        self._id = _id
        self.name = name
        self.sistema_solar_id = sistema_solar_id

class Luna:
    def __init__(self, _id, name, planeta_id):
        self._id = _id
        self.name = name
        self.planeta_id = planeta_id