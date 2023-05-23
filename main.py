
__version__ = "1.0.0"

import pyparsing
from kivy.lang import Builder
from kivymd.app import MDApp
from periodictable import formula


class ChemCalc(MDApp):
    def build(self):
        self.icon = "icon.png"
        return Builder.load_file('ChemCalc.kv')

    def amnt_func(self):
        mass = self.root.ids.mass.text
        molm = self.root.ids.molm.text
        try:
            amnt = float(mass)/float(molm)
        except:
            return self.mass_error()
        self.root.ids.amnt.text = str(amnt)

    def conc_func(self):
        amnt = self.root.ids.amnt.text
        volm = self.root.ids.volm.text
        try:
            conc = float(amnt)/float(volm)
        except:
            return self.volm_error()
        self.root.ids.conc.text = str(conc)

    def main_func(self):
        chem = self.root.ids.chem.text
        chem = chem.replace('[', '(').replace(']', ')')
        chem = chem.replace('*', '+').replace('•', '+').replace('@', '+')
        try:
            chem = formula(chem)
        except pyparsing.exceptions.ParseException:
            return self.chem_error()
        molm = chem.mass
        self.root.ids.molm.text = str(molm)
        if self.root.ids.mass.text != "":
            self.amnt_func()
        if self.root.ids.amnt.text != "" and self.root.ids.volm.text != "":
            self.conc_func()

    def chem_error(self):
        self.root.ids.chem.error = True

    def mass_error(self):
        self.root.ids.mass.error = True

    def volm_error(self):
        self.root.ids.volm.error = True


ChemCalc().run()
