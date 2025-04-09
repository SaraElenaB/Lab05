
class Studente:
    def __init__(self, matricola, cognome, nome, CDS):
        self.matricola = matricola
        self.cognome = cognome
        self.nome = nome
        self.cds = CDS

    def __str__(self):
        return f"""{self.nome.upper()}, {self.cognome.upper()} ({self.matricola})"""