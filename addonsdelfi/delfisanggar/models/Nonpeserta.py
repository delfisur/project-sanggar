from odoo import api, fields, models


class NonPeserta(models.Model):
    _name = 'delfisanggar.nonpeserta'
    _description = 'New Description'

    name = fields.Char(string='Name')
    no_hp = fields.Char(string='No Hp')
    