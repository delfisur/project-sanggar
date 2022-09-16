from odoo import api, fields, models


class KostumBaru(models.TransientModel):
    _name = 'delfisanggar.kostumbaru'
    _description = 'Kostum Baru'

    kostum_id = fields.Many2one(comodel_name='delfisanggar.kostum', string='Nama Kostum', required=True)
    jumlah = fields.Integer('Jumlah')

    def barang_datang(self):
        pass