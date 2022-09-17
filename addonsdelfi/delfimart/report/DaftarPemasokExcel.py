from odoo import models


class DaftarPemasok(models.AbstractModel):
    _name = 'report.delfimart.report_pemasok_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, pemasok):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        italic = workbook.add_format({'italic': True})
        row = 1
        col = 0
        sheet.write(row, col, 'Nama Pemasok', bold)
        sheet.write(row, col+1, 'Provinsi', bold)
        sheet.write(row, col+2, 'No Telepon', bold)
        for obj in pemasok:
            # report_name = obj.name
            row += 1
            col = 0
            sheet.write(row, col, obj.name, italic)
            sheet.write(row, col+1, obj.provinsi, italic)
            sheet.write(row, col+2, obj.no_telepon, italic)
            for xxx in obj.barang_ids:
                sheet.write(row, col+3, xxx.name, italic)
                col += 1
