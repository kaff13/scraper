import xlsxwriter as xls
from scrap import gen_data


def writer(data):
    book = xls.Workbook(r'C:\Users\HP\OneDrive\Рабочий стол\data.xlsx')
    page = book.add_worksheet('товар')

    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)

    for item in data:
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        row += 1

    book.close()


writer(gen_data())
