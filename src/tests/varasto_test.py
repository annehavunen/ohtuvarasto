import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.vikavarasto = Varasto(-1, -1)
        self.alkusaldopienempi = Varasto(10, 20)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # omat testit
    def test_virheellinen_tilavuus_on_nolla(self):
        self.assertAlmostEqual(self.vikavarasto.tilavuus, 0)

    def test_virheellinen_alkusaldo_on_nolla(self):
        self.assertAlmostEqual(self.vikavarasto.saldo, 0)

    def test_pienempi_alkusaldo_on_tilavuus(self):
        self.assertAlmostEqual(self.alkusaldopienempi.saldo, 10)

    def test_voi_lisata_vain_yli_nollan(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastoon_ei_voi_lisata_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
        
    def test_ei_voi_ottaa_alle_nollan(self):
        otettu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otettu, 0)

    def test_voi_ottaa_korkeintaan_saldon(self):
        otettu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(otettu, 0)

    def test_tulostus_on_oikein(self):
        tulostus = str(self.varasto)
        self.assertEqual(tulostus, "saldo = 0, vielä tilaa 100")
