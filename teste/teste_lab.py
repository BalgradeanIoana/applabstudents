import unittest

from ro.ubb.applabstudents.domain.lab import Laborator
from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, IncorectId, EntitateInexistenta, ValidatorException
from ro.ubb.applabstudents.domain.validators import LabValidator
from ro.ubb.applabstudents.repository.labsrepository import LaboratorRepository


class LabRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        lab1 = Laborator(1, 1, "descriere 1", 1)
        lab2 = Laborator(1, 2, "descriere 2", 1)
        self.validator = LabValidator()
        self.lab_repository = LaboratorRepository(self.validator)
        self.lab_repository.save(lab1)
        self.lab_repository.save(lab2)

    def test_find_all(self):
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 2)
        self.assertEqual(all_labs[0].get_id(), (1, 1))
        self.assertEqual(all_labs[0].get_descriere(), "descriere 1")
        self.assertEqual(all_labs[0].get_deadline(), 1)

    def test_save(self):
        lab = Laborator(2, 1, "descriere3", 2)
        self.lab_repository.save(lab)
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 3)
        self.assertEqual(all_labs[2].get_id(), (2,1))
        self.assertEqual(all_labs[2].get_descriere(), "descriere3")
        self.assertEqual(all_labs[2].get_deadline(), 2)
        self.assertRaises(IdDuplicat, self.lab_repository.save, lab)
        lab = Laborator(-1, 1, "descriere3", 2)
        self.assertRaises(ValidatorException, self.lab_repository.save, lab)
        lab = Laborator(1, -1, "descriere3", 2)
        self.assertRaises(ValidatorException, self.lab_repository.save, lab)

    def test_update(self):
        lab = Laborator(1, 1, "descriere3", 5)
        self.lab_repository.update(lab)
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 2)
        self.assertEqual(all_labs[0].get_id(), (1,1))
        self.assertEqual(all_labs[0].get_descriere(), "descriere3")
        self.assertEqual(all_labs[0].get_deadline(), 5)
        lab = Laborator(20, 1, "descriere3", 2)
        self.assertRaises(EntitateInexistenta, self.lab_repository.update, lab)


    def test_delete(self):
        self.lab_repository.delete_by_id((1,1))
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 1)
        self.assertEqual(all_labs[0].get_id(), (1, 2))
        self.assertEqual(all_labs[0].get_descriere(), "descriere 2")
        self.assertEqual(all_labs[0].get_deadline(), 1)
        self.assertRaises(EntitateInexistenta, self.lab_repository.delete_by_id, (20, 30))

    def test_find_by_id(self):
        lab = self.lab_repository.find_by_id((1, 1))
        all_labs = self.lab_repository.find_all()
        self.assertEqual(lab, all_labs[0])
        student = self.lab_repository.find_by_id(6)
        self.assertEqual(student, None)