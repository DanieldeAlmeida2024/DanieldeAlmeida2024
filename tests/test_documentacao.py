"""Verificações offline de integridade do README de perfil.

Não verifica autenticidade de credenciais nem disponibilidade de sites externos.
"""
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class TestesPerfil(unittest.TestCase):
    def test_conteudo_e_referencias_de_portfolio(self):
        for projeto in ("FoodBridge", "Panini Cards Check", "Modulock",
                        "Rastreamento de Veículos"):
            with self.subTest(projeto=projeto):
                self.assertIn(projeto, README)
        self.assertNotIn("casaconceitomarista", README.lower(),
                         "Projeto privado não deve ser destaque público")

    def test_certificacoes_aws_lado_a_lado_e_centralizadas(self):
        self.assertIn("AWS Academy · Cloud Foundations", README)
        self.assertIn("AWS re/Start · Graduate", README)
        bloco = re.search(
            r'<p align="center">(?P<conteudo>.*?Cloud Foundations.*?Graduate.*?)</p>',
            README, flags=re.DOTALL,
        )
        self.assertIsNotNone(bloco, "Não foi localizado o conjunto de badges centralizado")
        self.assertEqual(2, bloco.group("conteudo").count("<img "),
                         "Os dois badges devem permanecer no mesmo bloco sem tabela")
        self.assertIn("aws-cloud-banner.svg", README)
        self.assertNotIn("Outras credenciais serão adicionadas", README)

    def test_banner_aws_local_e_svg_valido(self):
        path = ROOT / "assets" / "aws-cloud-banner.svg"
        self.assertTrue(path.is_file())
        root = ElementTree.parse(path).getroot()
        self.assertEqual("{http://www.w3.org/2000/svg}svg", root.tag)
        self.assertTrue(any(x.tag.endswith("title") for x in root))

    def test_referencias_locais_do_readme_existem(self):
        for url in re.findall(r'(?:src|href)="(\./[^"]+)"', README):
            with self.subTest(url=url):
                self.assertTrue((ROOT / url).is_file(), f"Arquivo local ausente: {url}")

    def test_uml(self):
        conteudo = (ROOT / "docs" / "UML.puml").read_text(encoding="utf-8")
        self.assertIn("@startuml", conteudo)
        self.assertIn("@enduml", conteudo)


if __name__ == "__main__":
    unittest.main()
