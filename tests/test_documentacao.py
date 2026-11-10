import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class TestesPerfil(unittest.TestCase):
    def test_indice(self):
        texto=(R/'README.md').read_text(encoding='utf-8')
        self.assertIn('FoodBridge',texto)
        self.assertIn('Panini',texto)
    def test_uml(self):
        valor=(R/'docs/UML.puml').read_text(encoding='utf-8')
        self.assertIn('@startuml',valor)
        self.assertIn('@enduml',valor)
