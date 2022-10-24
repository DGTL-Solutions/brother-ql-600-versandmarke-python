import os
import time
import jinja2
import pdflatex
import subprocess

class Brother600qLableGenerator:
    def __init__(self):
        env = pdflatex.JINJA2_ENV
        env['loader'] = jinja2.FileSystemLoader(os.path.abspath('.'))
        env = jinja2.Environment(**env)
        self.template = env.get_template('Brother600qPrinterTemplatePostlableGermany.j2')

    def set_address(self, address: dict) -> None:
        '''
        Parameters:
            address (dict) = {
                name: str,
                surename: str,
                street_and_housenumber: str,
                postalcode: str,
                city: str,
                country: str
            }
        Returns:
            None
        '''

        self.address = address

    def generate(self) -> str:
        '''Generates PDF Lable and returns path+filename'''

        self.latex_lable_filename = str(int(time.time())) + ".tex"
        self.filename_without_suffix = self.latex_lable_filename.replace('.tex','')
        with open(self.latex_lable_filename,"w") as latex_lable:
           latex_lable.write(self.template.render(address=self.address))

        subprocess.call(["pdflatex","-interaction nonstopmode -halt-on-error -file-line-error",self.latex_lable_filename])
        subprocess.call(["rm",self.filename_without_suffix+".log",self.filename_without_suffix+".aux",self.filename_without_suffix+".tex"])

        self.pdf_lable_filename = self.latex_lable_filename.replace('.tex','.pdf')

        return self.pdf_lable_filename



    def print(self,delete_after_printing=True):
        subprocess.call(["lp","-o","media=Custom.62x35mm","-o","orientation-requested=5",self.pdf_lable_filename])
        if (delete_after_printing):
            subprocess.call(['rm',self.pdf_lable_filename])
