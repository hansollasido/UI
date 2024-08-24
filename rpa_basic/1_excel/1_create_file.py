from openpyxl import Workbook
wb = Workbook() 
ws = wb.active # 현재 활성화된 sheet를 가져옴
ws.title = "NadoSheet"
wb.save("sample.xlsx")
wb.close()