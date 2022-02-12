import pyttsx3
import PyPDF2
book=open('auditing.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
jarvis=pyttsx3.init()
for num in range(0, pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    jarvis.say(text)
    jarvis.runAndWait()