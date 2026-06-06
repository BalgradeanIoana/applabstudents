import unittest

from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, IncorectId, EntitateInexistenta
from ro.ubb.applabstudents.repository.labsrepository import LaboratorRepository
from ro.ubb.applabstudents.service.labsservice import LaboratorService


class LabServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.lab_repository = LaboratorRepository()
        self.lab_service = LaboratorService(self.lab_repository)
        self.lab_service.adaugare_laborator(1, 1, "descriere 1", 1)
        self.lab_service.adaugare_laborator(1, 2, "descriere 2", 2)

    def test_adaugare_laborator(self):
        self.lab_service.adaugare_laborator(2, 1, "descriere 3", 3)
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 3)
        self.assertEqual(all_labs[2].get_descriere(), "descriere 3")
        self.assertEqual(all_labs[2].get_deadline(), 3)
        self.assertRaises(IdDuplicat, self.lab_service.adaugare_laborator, 1, 1, "descriere 5", 5)
        self.assertRaises(IncorectId, self.lab_service.adaugare_laborator, -1, 4, "descriere 5", 5)
        self.assertRaises(IncorectId, self.lab_service.adaugare_laborator, 3, -4, "descriere 5", 5)

    def test_modifica_laborator(self):
        self.lab_service.modifica_laborator(1, 1, "descriere noua", 3)
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 2)
        self.assertEqual(all_labs[0].get_id(), (1,1))
        self.assertEqual(all_labs[0].get_descriere(), "descriere noua")
        self.assertEqual(all_labs[0].get_deadline(), 3)
        self.assertRaises(EntitateInexistenta, self.lab_service.modifica_laborator, 3, 1, "descriere noua", 3)
        self.assertRaises(EntitateInexistenta, self.lab_service.modifica_laborator, 1, 3, "descriere noua", 3)

    def test_stergere_laborator(self):
        self.lab_service.stergere_lab(1,1)
        all_labs = self.lab_repository.find_all()
        self.assertEqual(len(all_labs), 1)
        self.assertEqual(all_labs[0].get_id(), (1, 2))
        self.assertEqual(all_labs[0].get_descriere(), "descriere 2")
        self.assertEqual(all_labs[0].get_deadline(), 2)
        self.assertRaises(EntitateInexistenta, self.lab_service.stergere_lab, 6, 6)
