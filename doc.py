from docx import Document
import pyperclip

v = '1895.mp4'
print(pyperclip.paste())
doc = Document()

doc.add_paragraph(pyperclip.paste())
doc.save('./ocr _final/' + v[:-4] + '.docx')