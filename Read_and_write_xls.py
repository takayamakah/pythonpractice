from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 10
sheet['A2'] = 20
sheet['B1'] = 30
sheet['B2'] = 40

path = input('Qual caminho salvar o arquivo? ')
book.save(path)
