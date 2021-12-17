from openpyxl import Workbook

wb = Workbook()

planilha = wb.worksheets[0]

planilha['A1'] = "Banana"
planilha['B1'] = "Paçoca"

planilha.title = "planilha de frutas"
wb.save("C:/Users/lucaoliveira/Documents/PyAutoGui/MeuyArquivo2.xlsx")

