from odoo import fields, models, api


class Penyelenggara(models.Model):
    _inherit = 'res.partner'
    _description = 'Form Penyelenggara Didik Delcourse'

    is_tutor = fields.Boolean(
        string='Is Tutor',
        required=False)

    is_admin = fields.Boolean(
        string='Is Admin',
        required=False)