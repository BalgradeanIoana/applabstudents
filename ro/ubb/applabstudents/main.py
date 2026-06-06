import unittest

from ro.ubb.applabstudents.domain.validators import StudentValidator, LabValidator, NotaValidator
from ro.ubb.applabstudents.repository.lab_file_repository import LaboratorFileRepository
from ro.ubb.applabstudents.repository.nota_file_repository import NotaFileRepository
from ro.ubb.applabstudents.repository.student_file_repository import StudentFileRepository
from ro.ubb.applabstudents.service.labsservice import LaboratorService
from ro.ubb.applabstudents.service.noteservice import NoteService
from ro.ubb.applabstudents.service.studentsservice import StudentService
from ro.ubb.applabstudents.ui.consola import Consola
from ro.ubb.applabstudents.ui.uilabs import ConsolaLaborator
from ro.ubb.applabstudents.ui.uinota import ConsolaNota
from ro.ubb.applabstudents.ui.uistudents import ConsolaStudent
from ubb.applabstudents.service.reportsservice import ReportsService
from ubb.applabstudents.ui.uireports import ConsolaRaport


def all_test():
    unittest.main(verbosity=2)


def main():
    # teste_studenti()
    # teste_lab()
    #all_test()
    student_validator = StudentValidator()
    student_repository = StudentFileRepository(student_validator, "../../../data/students")
    student_service = StudentService(student_repository)
    consola_student = ConsolaStudent(student_service)

    lab_validator = LabValidator()
    laborator_repository = LaboratorFileRepository(lab_validator,"../../../data/labs")
    laborator_service = LaboratorService(laborator_repository)
    consola_laborator = ConsolaLaborator(laborator_service)

    nota_validator = NotaValidator()
    nota_repository = NotaFileRepository(nota_validator, "../../../data/nota")
    nota_service = NoteService(nota_repository)
    consola_nota = ConsolaNota(nota_service)

    raport_service = ReportsService(student_repository, laborator_repository, nota_repository)
    consola_raport = ConsolaRaport(raport_service)
    consola = Consola(consola_student, consola_laborator, consola_nota, consola_raport)
    consola.executa_meniu()

main()
#TODO: cand afisezi notele, afiseaza numele studentului, nu id-ul
#TODO: fa-ti documentatia la functii