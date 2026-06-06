from ubb.applabstudents.domain.exceptions import EntitateInexistenta


class ConsolaRaport:
    def __init__(self, rapoarte_service):
        self.__rapoarte_service = rapoarte_service

    def ui_afisare_studenti_ordonati_alfabetic_nota_lab_dat(self, nr_lab, nr_problema):
        try:
            dtos = self.__rapoarte_service.get_studenti_nota_lab(nr_lab, nr_problema)
            for dto in dtos:
                print(dto)
        except EntitateInexistenta as ei:
            print(ei)

    def ui_afiseaza_studenti_ordonati_alfabetic_medie_sub_5(self):
        dtos = self.__rapoarte_service.get_studenti_nota_sub_5()
        for dto in dtos:
            print(dto)



