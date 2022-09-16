from odoo import models


class ListPenyewaan(models.AbstractModel):
    _name = 'report.delfisanggar.report_penyewaan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, penyewaan):
        sheet = workbook.add_worksheet('List Penyewaan')
        bold = workbook.add_format({'bold': True})
        italic = workbook.add_format({'italic': True})
        row = 1
        col = 0
        sheet.write(row, col, 'Kode Penyewaan', bold)
        # sheet.write(row, col+1, 'Nama Penyewa', bold)
        sheet.write(row, col+1, 'Pembayaran', bold)
        for obj in penyewaan:
            # report_name = obj.name
            row += 1
            col = 0
            sheet.write(row, col, obj.kode, italic)
            # sheet.write(row, col+1, obj.user_id, italic)
            sheet.write(row, col+1, obj.bayar, italic)
            # for record in obj.list_ids:
            #     sheet.write(row, col+3, record.kostum_id, italic)
            #     col += 1