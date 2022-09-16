from odoo import api, fields, models


class Pelatih(models.Model):
    _name = 'delfisanggar.pelatih'
    _description = 'Pelatih Tari'

    name = fields.Char(string='Nama Pelatih')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telp')
    
    jadwal_ids = fields.One2many(comodel_name='delfisanggar.jadwal', inverse_name='pelatih_id', string='Jadwal')
    