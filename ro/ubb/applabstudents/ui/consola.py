


class Consola:
    def __init__(self, consola_student, consola_lab, consola_nota, consola_rapoarte):
        self.__consola_student = consola_student
        self.__consola_lab = consola_lab
        self.__consola_nota = consola_nota
        self.__consola_rapoarte = consola_rapoarte

    def executa_meniu(self):
        comenzi_dict = {"adauga_student": self.__consola_student.ui_adauga_student, "afisare_studenti": self.__consola_student.ui_afisare_studenti,
                        "modifica_student": self.__consola_student.ui_modificare_student, "sterge_student": self.__consola_student.ui_stergere_student,
                        "adauga_laborator": self.__consola_lab.ui_adauga_laborator, "afisare_laboratoare": self.__consola_lab.ui_afisare_laboratoare,
                        "modifica_laborator": self.__consola_lab.ui_modifica_laborator, "sterge_laborator": self.__consola_lab.ui_sterge_laborator,
                        "adauga_nota": self.__consola_nota.ui_adauga_nota, "afisare_note": self.__consola_nota.ui_afisare_note,
                        "modifica_nota": self.__consola_nota.ui_modifica_nota, "sterge_nota": self.__consola_nota.ui_sterge_nota,
                        "lista_studenti_note_la_un_lab": self.__consola_rapoarte.ui_afisare_studenti_ordonati_alfabetic_nota_lab_dat,
                        "lista_studenti_medie_sub_5": self.__consola_rapoarte.ui_afiseaza_studenti_ordonati_alfabetic_medie_sub_5,
                        "help": self.__help}
        while(True):
            try:
                print("Alegeti o comanda sau help pentu ajutor (help <nume_comanda>):",end="\n\t")
                print(*comenzi_dict.keys(), "exit", sep = "\n\t", end="\n\t")
                comanda, arg = self.__citire_comanda()
                if comanda == "exit":
                    break
                comenzi_dict[comanda](*arg)
            except KeyError as ke:
                print("Comanda invalida. Asigurativa ca ati introdus o comanda din lista de mai sus")
            except TypeError as te:
                print("Pentru aceasta comanda se asteapta si niste argumente. Incercati optiunea help <comanda> pentru ajutor")

    def __help(self, comanda):
        help_dict  = {"adauga_student": "adauga_student <id>,<nume>,<grupa>", "afiseaza_studenti": "afiseaza_studenti",
                      "modifica_student": "modifica_student <id>,<nume(nou)>,<grupa(noua)>", "sterge_student": "sterge_student <id>",
                      "adauga_laborator": "adauga_laborator <nr_lab>,<nr_problema>,<descriere>,<deadline(numarul unei saptamani)>",
                      "afisare_laborator": "afisare_laborator", "sterge_laborator": "sterge_laborator <nr_lab>,<nr_problema>",
                      "modifica_laborator": "modifica_laborator <nr_lab>,<nr_problema>,<descriere(noua)>,<deadline(nou)>",
                      "adauga_nota": "adauga_nota <student_id>,<nr_lab>,<nr_problema>,<nota>", "afiseaza_note": "afiseaza_note",
                      "modifica_nota": "modifica_nota <student_id>,<nr_lab>,<nr_problema>,<nota(noua)>",
                      "sterge_nota": "sterge_nota <student_id>,<nr_lab>,<nr_problema>",
                      "lista_studenti_note_la_un_lab": "lista_studenti_note_la_un_lab <nr_lab>,<nr_problema>",
                      "lista_studenti_medie_sub_5": "lista_studenti_medie_sub_5"}
        print("Utilizare: ", help_dict[comanda])

    def __citire_comanda(self):
        linie = input()
        poz = linie.find(" ")
        if poz == -1:
            return linie, []
        comanda = linie[:poz]
        args = linie[poz + 1:]
        args = args.split(",")
        args = [el.strip() for el in args]
        return comanda, args
