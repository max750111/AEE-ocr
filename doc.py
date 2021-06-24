from docx import Document
import pyperclip

print(pyperclip.paste())
doc = Document()

doc.add_paragraph(pyperclip.paste())
doc.save('demo.docx')