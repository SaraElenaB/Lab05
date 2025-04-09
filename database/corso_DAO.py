# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

class CorsoDAO():

    def __init__(self):
        self.dbConnect = DBConnect()

    #-----------------------------------------------------------------------------------------------------------------------------
    def getCorsi(self):

        cnx= self.dbConnect.get_connection()
        cursor=cnx.cursor( dictionary=True )
        query=""" SELECT * FROM corso"""
        cursor.execute(query)

        corsi=[]
        for row in cursor:
            corsi.append( Corso( row["codins"], row["crediti"], row["nome"], row["pd"] ) )

        cursor.close()
        cnx.close()
        return corsi

    # -----------------------------------------------------------------------------------------------------------------------------
    def getIscritti(self, corso):

        cnx= self.dbConnect.get_connection()
        cursor=cnx.cursor( dictionary=True )
        query=""" SELECT * FROM studente, iscrizione WHERE studente.matricola=iscrizione.matricola AND iscrizione.codins=%s """
        cursor.execute(query, (corso,) )

        studenti = []
        for r in cursor:
            studenti.append( Studente( r["matricola"], r["cognome"], r["nome"], r["CDS"] ))

        cursor.close()
        cnx.close()
        return studenti

    # -----------------------------------------------------------------------------------------------------------------------------
    # def getCorsiPerStudente(self, matricola):
    #
    #     cnx = self.dbConnect.get_connection()
    #     cursor = cnx.cursor(dictionary=True)
    #     query = """ SELECT * FROM corso WHERE studente.matricola=%s"""
    #     cursor.execute(query, (matricola,) )
    #
    #     corsi=[]
    #     for row in cursor:
    #         corsi.append( Corso( row["codins"], row["crediti"], row["nome"], row["pd"]))
    #
    #     cursor.close()
    #     cnx.close()
    #     return corsi
