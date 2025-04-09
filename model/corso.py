class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codiceInsegnamento= codins
        self.crediti= crediti
        self.nome= nome
        self.pd= pd

    def __str__(self):
        return f" {self.nome} ({self.codiceInsegnamento})"