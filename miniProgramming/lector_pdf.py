import PyPDF2, pyttsx3

path = open('leer.pdf', 'rb')

pdfReader =  PyPDF2.PdfFileReader(path)

speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()