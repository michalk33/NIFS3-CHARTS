"""
interface.py
====================================
Moduł implementujący interfejs.
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import events as ev
import reading as rd


class MainWindow(Gtk.Window):
    """Główne okno interfejsu

    Attributes
    ----------
    chosen_file : str
        Ścieżka do otwieranego pliku.
    fname
        Element interfejsu.
    project_name
        Element interfejsu.
    project_name2
        Element interfejsu.
    num_points
        Element interfejsu.
    lbl4
        Element interfejsu.
    tmplam
        Pomocnicza lambda.

    """
    def __init__(self):
        """Konstruktor głównego okna - nie przyjmuje żadnych argumentów
        
        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        super().__init__(title="NIFS3 charts")
        self.set_border_width(5)

        self.chosen_file = "No file chosen"

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        main_stack = Gtk.Stack()
        main_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_stack.set_transition_duration(250)

        self.fname = Gtk.Label()
        self.fname.set_markup(self.chosen_file)
        btn_chsf = Gtk.Button(label="Choose File")
        btn_chsf.connect("clicked", self.choose_file)
        lbl1 = Gtk.Label()
        lbl1.set_markup("<big><b>Project name:</b></big>")
        self.project_name = Gtk.Entry()
        btn_crpr = Gtk.Button(label="Create project")
        btn_crpr.connect("clicked", self.create_project)
        vbox1.pack_start(self.fname, True, True, 0)
        vbox1.pack_start(btn_chsf, True, True, 0)
        vbox1.pack_start(lbl1, True, True, 0)
        vbox1.pack_start(self.project_name, True, True, 0)
        vbox1.pack_start(btn_crpr, True, True, 0)
        main_stack.add_titled(vbox1, "newproject", "New project")

        lbl2 = Gtk.Label()
        lbl2.set_markup("<big><b>Project name:</b></big>")
        self.project_name2 = Gtk.Entry()
        lbl3 = Gtk.Label()
        lbl3.set_markup("<big><b>Number of points:</b></big>")
        self.num_points = Gtk.Entry()
        btn_crt = Gtk.Button(label="Save chart")
        btn_crt_d = Gtk.Button(label="Save chart data")
        btn_crt.connect("clicked", self.crt_chart)
        btn_crt_d.connect("clicked", self.crt_chart_d)
        vbox2.pack_start(lbl2, True, True, 0)
        vbox2.pack_start(self.project_name2, True, True, 0)
        vbox2.pack_start(lbl3, True, True, 0)
        vbox2.pack_start(self.num_points, True, True, 0)
        vbox2.pack_start(btn_crt, True, True, 0)
        vbox2.pack_start(btn_crt_d, True, True, 0)
        main_stack.add_titled(vbox2, "newchart", "New chart")

        self.lbl4 = Gtk.Label()
        self.tmplam = lambda x: "".join(s+"; " for s in x[0])
        prnames = rd.read_projects()
        if prnames == []:
            self.lbl4.set_markup("")
        else:
            self.lbl4.set_markup(self.tmplam(prnames))
        vbox3.pack_start(self.lbl4, True, True, 0)
        main_stack.add_titled(vbox3, "listpr", "List of projects")

        main_stack_switcher = Gtk.StackSwitcher()
        main_stack_switcher.set_stack(main_stack)

        vbox.pack_start(main_stack_switcher, True, True, 0)
        vbox.pack_start(main_stack, True, True, 0)

    def choose_file(self, widget):
        """Metoda odpowiedzialna za wybór pliku do otwarcia

        Returns
        -------
        None

        """
        wnd = Gtk.FileChooserDialog(title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN)
        wnd.add_buttons(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK)
        self.add_filters(wnd)
        ret = wnd.run()
        if ret == Gtk.ResponseType.OK:
            self.chosen_file = wnd.get_filename()
            self.fname.set_markup(wnd.get_filename())
        wnd.destroy()

    def create_project(self, widget):
        """Metoda odpowiedzialna za obsługę dodania nowego projektu

        Returns
        -------
        None

        """
        ret = ev.check_new_project(self.chosen_file, self.project_name.get_text())
        if ret == 1:
            question = Gtk.Dialog(title="Warning", parent=self, flags=0)
            question.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
            question.set_default_size(150, 100)
            qlbl = Gtk.Label(label="Do you want to overwrite an existing project?")
            qbox = question.get_content_area()
            qbox.add(qlbl)
            question.show_all()

            res = question.run()
            if res == Gtk.ResponseType.OK:
                ret = 2
            else:
                ret = 0

            question.destroy()

        if ret == 2:
            if ev.add_new_project(self.chosen_file, self.project_name.get_text()):
                msg1 = Gtk.Dialog(title="Warning", parent=self, flags=0)
                msg1.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
                msg1.set_default_size(150, 100)
                msg1lbl = Gtk.Label(label="The new project created succesfully.")
                msg1box = msg1.get_content_area()
                msg1box.add(msg1lbl)
                msg1.show_all()
                msg1.run()
                msg1.destroy()
            else:
                msg2 = Gtk.Dialog(title="Warning", parent=self, flags=0)
                msg2.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
                msg2.set_default_size(150, 100)
                msg2lbl = Gtk.Label(label="Something went wrong.")
                msg2box = msg2.get_content_area()
                msg2box.add(msg2lbl)
                msg2.show_all()
                msg2.run()
                msg2.destroy()

        prnames = rd.read_projects()
        if prnames == []:
            self.lbl4.set_markup("")
        else:
            self.lbl4.set_markup(self.tmplam(prnames))


    def add_filters(self, wnd):
        """Metoda pomocnicza do konstrukcji okna wyboru pliku.

        Returns
        -------
        None

        """
        csvft = Gtk.FileFilter()
        csvft.set_name("CSV files")
        csvft.add_mime_type("text/csv")
        wnd.add_filter(csvft)
        anyft = Gtk.FileFilter()
        anyft.set_name("All files")
        anyft.add_pattern("*")
        wnd.add_filter(anyft)

    def add_filters2(self, wnd):
        """Metoda pomocnicza do konstrukcji okna wyboru pliku.

        Returns
        -------
        None

        """
        csvft = Gtk.FileFilter()
        csvft.set_name("PNG files")
        csvft.add_mime_type("image/png")
        wnd.add_filter(csvft)
        anyft = Gtk.FileFilter()
        anyft.set_name("All files")
        anyft.add_pattern("*")
        wnd.add_filter(anyft)

    def crt_chart(self, widget):
        """Metoda odpowiedzialna za utworzenie wykresu.

        Returns
        -------
        None

        """
        if ev.check_new_chart(self.project_name2.get_text(), self.num_points.get_text()):
            wnd = Gtk.FileChooserDialog(title="Please choose a file", parent=self, action=Gtk.FileChooserAction.SAVE)
            wnd.add_buttons(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK)
            self.add_filters2(wnd)
            ret = wnd.run()
            if ret == Gtk.ResponseType.OK:
                self.chosen_file = wnd.get_filename()
                self.fname.set_markup(wnd.get_filename())
                res = 1
            else:
                res = 0
            wnd.destroy()
            if res:
                if ev.save_new_chart(self.chosen_file, self.project_name2.get_text(), self.num_points.get_text()):
                    msg1 = Gtk.Dialog(title="Warning", parent=self, flags=0)
                    msg1.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
                    msg1.set_default_size(150, 100)
                    msg1lbl = Gtk.Label(label="The new chart created succesfully.")
                    msg1box = msg1.get_content_area()
                    msg1box.add(msg1lbl)
                    msg1.show_all()
                    msg1.run()
                    msg1.destroy()
                else:
                    msg2 = Gtk.Dialog(title="Warning", parent=self, flags=0)
                    msg2.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
                    msg2.set_default_size(150, 100)
                    msg2lbl = Gtk.Label(label="Something went wrong.")
                    msg2box = msg2.get_content_area()
                    msg2box.add(msg2lbl)
                    msg2.show_all()
                    msg2.run()
                    msg2.destroy()

    def crt_chart_d(self, widget):
        """Metoda odpowiedzialna za utworzenie pliku danych wykresu.

        Returns
        -------
        None

        """
        if ev.check_new_chart(self.project_name2.get_text(), self.num_points.get_text()):
            wnd = Gtk.FileChooserDialog(title="Please choose a file", parent=self, action=Gtk.FileChooserAction.SAVE)
            wnd.add_buttons(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK)
            self.add_filters(wnd)
            ret = wnd.run()
            if ret == Gtk.ResponseType.OK:
                self.chosen_file = wnd.get_filename()
                self.fname.set_markup(wnd.get_filename())
                res = 1
            else:
                res = 0
            wnd.destroy()
            if res:
                if ev.save_new_chart_d(self.chosen_file, self.project_name2.get_text(), self.num_points.get_text()):
                    msg1 = Gtk.Dialog(title="Warning", parent=self, flags=0)
                    msg1.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
                    msg1.set_default_size(150, 100)
                    msg1lbl = Gtk.Label(label="The new chart data created succesfully.")
                    msg1box = msg1.get_content_area()
                    msg1box.add(msg1lbl)
                    msg1.show_all()
                    msg1.run()
                    msg1.destroy()
                else:
                    msg2 = Gtk.Dialog(title="Warning", parent=self, flags=0)
                    msg2.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
                    msg2.set_default_size(150, 100)
                    msg2lbl = Gtk.Label(label="Something went wrong.")
                    msg2box = msg2.get_content_area()
                    msg2box.add(msg2lbl)
                    msg2.show_all()
                    msg2.run()
                    msg2.destroy()
