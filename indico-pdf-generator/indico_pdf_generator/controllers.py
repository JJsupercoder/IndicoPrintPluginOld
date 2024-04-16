from indico.core.plugins import IndicoPlugin
from flask import render_template
from indico_pdf_generator import PDFGeneratorPlugin


class PDFGenerator(IndicoPlugin):
    """PDF Generator Plugin"""

    def init(self):
        super(PDFGenerator, self).init()

    def get_blueprints(self):
        from .blueprint import blueprint

        return blueprint

    def get_templates_path(self):
        return self.root_path


__plugin__ = PDFGenerator
