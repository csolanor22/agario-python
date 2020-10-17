
class iterator():
    def __init__(self, data):
        self.agregado = data
        self.conteo = 0

    def has_next(self):
        if self.conteo <= (len(self.agregado)-1):
            dato = self.agregado[self.conteo]
            self.conteo = self.conteo + 1
            return dato          
        else:
            self.conteo = 0
            return None
        