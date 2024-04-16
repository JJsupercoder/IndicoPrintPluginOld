from __future__ import unicode_literals
from setuptools import setup

setup(
    name="indico-pdf-generator",
    version="0.1",
    packages=["indico_pdf_generator"],
    platforms="any",
    install_requires=["indico>=2.0.dev0", "Flask"],
    entry_points={
        "indico.plugins": {
            "indico_pdf_generator = indico_pdf_generator:PDFGeneratorPlugin"
        }
    },
)
