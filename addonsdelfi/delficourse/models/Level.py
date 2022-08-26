from odoo import fields, models, api


class Level(models.Model):
    _name = 'delficourse.level'
    _description = 'Pendaftaran Level'

    name = fields.Selection(
        string='Nama Level',
        selection=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    keterangan = fields.Char(
        string='Keterangan')
    biaya = fields.Integer(
        string='Biaya')

    course_ids = fields.One2many(
        comodel_name='delficourse.pendaftaran',
        inverse_name='level_belajar',
        string='Daftar Kursus',
        required=False)