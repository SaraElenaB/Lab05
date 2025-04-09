from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO

class Model:

    def __init__(self):
        self.corsoDAO = CorsoDAO()
        self.studenteDao = StudenteDAO()

    def getCorsi(self):
        return self.corsoDAO.getCorsi()

    def getIscritti(self, corso):
        return self.corsoDAO.getIscritti(corso)

    def get_studente(self, matricola):
        return self.studenteDao.getStudente(matricola)

    def getCorsiDelloStudente(self, matricola):
        return self.studenteDao.getCorsiPerStudente(matricola)