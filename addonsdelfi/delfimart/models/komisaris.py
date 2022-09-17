from odoo import api, fields, models


class Komisaris(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    jabatan = fields.Selection([('komut', 'Komisaris Utama'), ('anggota', 'Komisaris')],
        string='Jabatan')

class Direksi(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    jabatan_direksi = fields.Selection([('direkut', 'Direksi Utama'), ('direksi', 'Direksi')], string='Jabatan Direksi')
