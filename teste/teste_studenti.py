import unittest

from ro.ubb.applabstudents.domain.student import Student
from ro.ubb.applabstudents.repository.studentsrepository import StudentRepository
from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, IncorectId, EntitateInexistenta


class StudentRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        student1 = Student(1, "studentul 1", 1511)
        student2 = Student(2, "studentul 2", 311)
        self.student_repository = StudentRepository()
        self.student_repository.save(student1)
        self.student_repository.save(student2)

    def test_find_all(self):
        all_student = self.student_repository.find_all()
        self.assertEqual(len(all_student), 2)
        self.assertEqual(all_student[0].get_id(), 1)
        self.assertEqual(all_student[0].get_nume(), "studentul 1")
        self.assertEqual(all_student[0].get_grupa(), 1511)

    def test_save(self):
        student = Student(3, "studentul3", 1511)
        self.student_repository.save(student)
        all_student = self.student_repository.find_all()
        self.assertEqual(len(all_student), 3)
        self.assertEqual(all_student[2].get_id(), 3)
        self.assertEqual(all_student[2].get_nume(), "studentul3")
        self.assertEqual(all_student[2].get_grupa(), 1511)
        student = Student(3, "studentul3", 1511)
        self.assertRaises(IdDuplicat, self.student_repository.save, student)
        student = Student(-1, "studentul3", 1511)
        self.assertRaises(IncorectId, self.student_repository.save, student)

    def test_update(self):
        student = Student(1, "studentul3", 311)
        self.student_repository.update(student)
        all_student = self.student_repository.find_all()
        self.assertEqual(len(all_student), 2)
        self.assertEqual(all_student[0].get_id(), 1)
        self.assertEqual(all_student[0].get_nume(), "studentul3")
        self.assertEqual(all_student[0].get_grupa(), 311)
        student = Student(100, "studentul3", 311)
        self.assertRaises(EntitateInexistenta, self.student_repository.update, student)

    def test_delete(self):
        self.student_repository.delete_by_id(1)
        all_student = self.student_repository.find_all()
        self.assertEqual(len(all_student), 1)
        self.assertEqual(all_student[0].get_id(), 2)
        self.assertEqual(all_student[0].get_nume(), "studentul 2")
        self.assertEqual(all_student[0].get_grupa(), 311)
        student = Student(100, "studentul3", 311)
        self.assertRaises(EntitateInexistenta, self.student_repository.delete_by_id, student)

    def test_find_by_id(self):
        student = self.student_repository.find_by_id(1)
        all_student = self.student_repository.find_all()
        self.assertEqual(student, all_student[0])
        student = self.student_repository.find_by_id(6)
        self.assertEqual(student, None)


