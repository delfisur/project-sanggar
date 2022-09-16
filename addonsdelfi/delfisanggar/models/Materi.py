from odoo import api, fields, models


class Materi(models.Model):
    _name = 'delfisanggar.materi'
    _description = 'Materi'

    name = fields.Char(string='Nama Tari')
    durasi = fields.Char(string='Durasi Tari')

    # level_ids = fields.One2many(comodel_name='delfisanggar_level', inverse_name='nama_tari', string='Tingkatan Kelas')
    
