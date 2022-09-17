from odoo import models, fields, api


class Kasir(models.Model):
    _name = 'delfimart.kasir'
    _inherit = 'delfimart.person'
    _description = 'Grup Delfimart'

    id_pegawai = fields.Char(string='ID Pegawai')
    status_pegawai = fields.Selection(
        [('kontrak', 'Kontrak'),
        ('tetap', 'Tetap'),
        ('magang', 'Magang')],string='Status Pegawai')
    
    
    