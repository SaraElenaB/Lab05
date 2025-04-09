import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view    #graphical elements of the UI
        self._model = model  #logic of the program and holds the data

    #------------------------------------------------------------------------------------------------------------------------------
    def listaCorsi(self):

        lista = []
        corsi = self._model.getCorsi()
        for c in corsi:
            lista.append( ft.dropdown.Option( key=c.codiceInsegnamento, text=c.__str__() ) )
        return lista

    # ------------------------------------------------------------------------------------------------------------------------------
    def handleCercaIscritti(self, e): #e perchè c'è on_click

        if (self._view._menuCorso.value is None) or (self._view._menuCorso.value == ""):
            self._view.create_alert("Selezionare un corso!")
            return
        else:
            iscritti= self._model.getIscritti( self._view._menuCorso.value)
            nomeCorso= self._view._menuCorso.value
            self._view.txt_listaIscritti.controls.clear()
            self._view.txt_listaIscritti.controls.append( ft.Text( f"Ci sono {len(iscritti)} studenti al corso {nomeCorso}:" ))
            for s in iscritti:
                self._view.txt_listaIscritti.controls.append( ft.Text( f"{s.__str__()}"))
            self._view.update_page()

    # ------------------------------------------------------------------------------------------------------------------------------
    def handleCercaStudente(self, e):

        if (self._view._txtMatricola.value is None) or (self._view._txtMatricola.value == ""):
            self._view.create_alert("Selezionare una matricola!")
            return
        elif not self._view._txtMatricola.value.isnumeric():
            self._view.create_alert("La matricola è un numero composto da 6 cifre!")
            return
        elif self._model.get_studente( self._view._txtMatricola.value) is None:
            self._view.create_alert("Non esiste nessun studente con questa matricola!")
            return
        else:
            studente = self._model.get_studente( int(self._view._txtMatricola.value) ) #oggetto
            self._view._txtNome.value = studente.nome
            self._view._txtCognome.value = studente.cognome
            self._view.update_page()
            # self._view._txtCognome.controls.clear()
            # self._view._txtCognome.controls.append(ft.Text(f"{studente.cognome}"))

    # ------------------------------------------------------------------------------------------------------------------------------
    def handleCercaCorso(self, e):

        if self._view._txtMatricola.value is None or self._view._txtMatricola.value == "":
            self._view.create_alert("Selezionare una matricola!")
            return
        else:
            matricola = self._view._txtMatricola.value
            listaCorsiDelloStudente = self._model.getCorsiDelloStudente(matricola)

            if len(listaCorsiDelloStudente) == 0:
                self._view.txt_listaCorsi.controls.append( ft.Text("Lo studente non è iscritto a nessun corso"))
                self._view.update_page()
                return

            self._view.txt_listaCorsi.controls.append(ft.Text(f"Risultano {len(listaCorsiDelloStudente)} corsi:"))
            for corso in listaCorsiDelloStudente:
                self._view.txt_listaCorsi.controls.append( ft.Text(f"{corso.__str__()}"))
            self._view.update_page()





