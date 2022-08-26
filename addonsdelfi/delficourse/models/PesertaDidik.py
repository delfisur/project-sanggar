from odoo import fields, models, api


class PesertaDidik(models.Model):
    _inherit = 'res.partner'
    _description = 'Form Peserta Didik Delcourse'

    jenis_kursus = fields.Selection(selection=[('pemprograman', 'Pemprograman'), ('bahasa', 'Bahasa'), ('keterampilan', 'Keterampilan')],
        string='Jenis Kursus',
        required=False)
    
    is_peserta = fields.Boolean(
        string='Is_peserta', 
        required=False)

    kursus = fields.Many2one(
        comodel_name='delficourse.sessionpemprograman',
        string='Kursus',
        required=False)