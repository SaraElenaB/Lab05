# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import DBConnect
from model.studente import Studente
from model.corso import Corso

class StudenteDAO():

    def __init__(self):
        self.dbConnect = DBConnect()

    # -----------------------------------------------------------------------------------------------------------------------------
    def getStudente(self, matricola):

        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM studente WHERE studente.matricola=%s"""
        cursor.execute(query, (matricola,) )

        sTemp = cursor.fetchone() #altrimenti si arrabbia
        if sTemp is None:
            return None
        studente = Studente( sTemp["matricola"], sTemp["cognome"], sTemp["nome"], sTemp["CDS"])
        cursor.close()
        cnx.close()
        return studente

    # -----------------------------------------------------------------------------------------------------------------------------
    def getCorsiPerStudente(self, matricola):

        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM corso, iscrizione WHERE iscrizione.matricola=%s AND iscrizione.codins=corso.codins"""
        cursor.execute(query, (matricola,))

        corsi = []
        for row in cursor:
            corsi.append( Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

        cursor.close()
        cnx.close()
        return corsi
#from database.DB_connect import get_connection
