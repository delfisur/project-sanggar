from odoo import api, fields, models


class Level(models.Model):
    _name = 'delfisanggar.level'
    _description = 'Level Kelas'

    name = fields.Selection(string='Level Kelas', selection=[('pemula','Pemula'),('terampil','Terampil'),('mahir','Mahir')], required=True)
    deskripsi = fields.Char(string='Deskripsi')
    biaya = fields.Integer(string='Biaya')

    # nama_tari = fields.Many2one(comodel_name='delfisanggar.materi', string='Nama Tari')
    
    
    