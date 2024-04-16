from __future__ import unicode_literals

from flask_pluginengine import PluginBase

class PDFGeneratorPlugin(PluginBase):
    def init(self):
        super(PDFGeneratorPlugin, self).init()

__all__ = ('PDFGeneratorPlugin',)
