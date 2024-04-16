Use the plugin.

1. Incase plugin doesnt work, try changing the content in MANIFEST.in to the following lines below:

graft indico_pdf_generator/static
graft indico_pdf_generator/templates
global-exclude \*.pyc **pycache** .keep

2. If nothing works, contact the author Jenson Joseph with the issue.
