import xlsxwriter

file = open("Result/juniper.txt", 'r')
data = file.readlines()
workbook = xlsxwriter.Workbook('Result/juniper.xlsx')
worksheet = workbook.add_worksheet('Result')
format = workbook.add_format({'bold': True, 'align': 'center'})
format.set_border()
format.set_pattern(1)
format.set_bg_color('#A9BCF5')

format2 = workbook.add_format()
format2.set_border()
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('G:G', 15)
worksheet.set_column('H:H', 15)
worksheet.set_column('K:K', 15)
worksheet.set_column('L:L', 15)
worksheet.set_column('M:M', 15)

worksheet.write(0, 0, 'Hostname', format)
worksheet.write(0, 1, 'IP', format)
worksheet.write(0, 2, 'Model', format)
worksheet.write(0, 3, 'Serial', format)
worksheet.write(0, 4, 'Memory', format)
worksheet.write(0, 5, 'CPU', format)
worksheet.write(0, 6, 'Module', format)
worksheet.write(0, 7, 'Power', format)
worksheet.write(0, 8, 'Fan', format)
worksheet.write(0, 9, 'Interface', format)
worksheet.write(0, 10, 'Version', format)
worksheet.write(0, 11, 'Log', format)
worksheet.write(0, 12, 'Alarm', format)

row = 1
col = 0

for i in data:
    for j in i.split('|'):
        worksheet.write(row, col, j, format2)
        col += 1
    col = 0
    row += 1

workbook.close()
