import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""

        # title
        self._title = ft.Text("App Gestione Studenti",
                              color="blue", size=24) #non c'è bisogno dell'aligment perchè è automatico?
        self._page.controls.append(self._title)      #append prende solo un argomento alla volta

        #row 1: corso + cerca iscritti
        self._menuCorso = ft.Dropdown( hint_text="Selezionare un corso",
                                       label="Corso",
                                       width=200,
                                       options= self._controller.listaCorsi(),
                                       #filled = True,  # Sfondo colorato
                                       expand = True,  # Occupa tutto lo spazio disponibile
                                       #options=[ft.dropdown.Option("mat101", "Matematica")
                                       )
        #self.txtScegli = ft.Column( controls=[ ft.Text("Seleziona un corso"), self._menuCorso])
        self._btnIscritti = ft.ElevatedButton( text="Cerca Iscritti",
                                               width=150,
                                               on_click= self._controller.handleCercaIscritti)

        self._row1= ft.Row( [self._menuCorso, self._btnIscritti], alignment=ft.MainAxisAlignment.CENTER ) #in questo modo si allineano
        self._page.controls.append(self._row1)

        #row2: matricola + nome + cognome --> nome/cognome non editabili
        self._txtMatricola= ft.TextField( label="Matricola",
                                           width=200)
        self._txtNome= ft.TextField( label="Nome",
                                      width=200, read_only=True)
        self._txtCognome= ft.TextField( label="Cognome",
                                        width=200, read_only=True)
        self._row2= ft.Row( [self._txtMatricola, self._txtNome, self._txtCognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(self._row2)

        #row3: cerca studente
        self._btnStudente = ft.ElevatedButton( text="Cerca Studente",
                                               width=150,
                                               on_click= self._controller.handleCercaStudente )
        self._btnCorso = ft.ElevatedButton( text="Cerca Corso",
                                            width=150,
                                            on_click= self._controller.handleCercaCorso)

        self._row3= ft.Row( [self._btnStudente, self._btnCorso], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(self._row3)



        # List View where the reply is printed
        self.txt_listaIscritti = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_listaIscritti)
        self.txt_listaCorsi = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_listaCorsi)
        self._page.update()

    #------------------------------------------------------------------------------------------------------------------------------------
    #getter and setter
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
