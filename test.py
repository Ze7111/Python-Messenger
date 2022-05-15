from xlrd import open_workbook

book = open_workbook('example.xlsx')
sheet = book.sheet_by_index(0)
collection_year_col = 2 #Just an example
test_year = 2010
for row in range(sheet.nrows):
    if sheet.cell(row,collection_year_col).value == test_year:
        print("found")