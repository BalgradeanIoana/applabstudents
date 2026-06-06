import unittest

from ro.ubb.applabstudents.repository.studentsrepository import StudentRepository
from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, IncorectId, EntitateInexistenta
from ro.ubb.applabstudents.service.studentsservice import StudentService


class StudentServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.student_service = StudentService(self.student_repository)
        self.student_service.adaugare_student(1, "studentul 1", 1511)
        self.student_service.adaugare_student(2, "studentul 2", 311)

    def test_adaugare_student(self):
        self.student_service.adaugare_student(3, "studentul 3", 1511)
        all_students = self.student_repository.find_all()
        self.assertEqual(len(all_students), 3)
        self.assertEqual(all_students[2].get_id(), 3)
        self.assertEqual(all_students[2].get_nume(), "studentul 3")
        self.assertEqual(all_students[2].get_grupa(), 1511)
        self.assertRaises(IdDuplicat, self.student_service.adaugare_student, 1, "studentul 4", 1511)
        self.assertRaises(IncorectId, self.student_service.adaugare_student, -1, "studentul 4", 311)

    def test_modifica_student(self):
        self.student_service.modifica_student(1, "studentul 4", 311)
        all_students = self.student_repository.find_all()
        self.assertEqual(len(all_students), 2)
        self.assertEqual(all_students[0].get_id(), 1)
        self.assertEqual(all_students[0].get_nume(), "studentul 4")
        self.assertEqual(all_students[0].get_grupa(), 311)
        self.assertRaises(EntitateInexistenta, self.student_service.modifica_student, 6, "studentul 4", 311)

    def test_stergere_student(self):
        self.student_service.stergere_student(1)
        all_students = self.student_repository.find_all()
        self.assertEqual(len(all_students), 1)
        self.assertEqual(all_students[0].get_id(), 2)
        self.assertEqual(all_students[0].get_nume(), "studentul 2")
        self.assertEqual(all_students[0].get_grupa(), 311)
        self.assertRaises(EntitateInexistenta, self.student_service.stergere_student, 6)