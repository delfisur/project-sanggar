from odoo import api, fields, models


class Jadwal(models.Model):
    _name = 'delfisanggar.jadwal'
    _description = 'Jadwal'
    name = fields.Char()
    

    pelatih_id = fields.Many2one(comodel_name='delfisanggar.pelatih', string='Pelatih Tari')
    materi_id = fields.Many2one(comodel_name='delfisanggar.materi', string='Materi Tari')
    hari = fields.Char(string='Hari')
    jam = fields.Char(string='Jam')
    kelas_id = fields.Many2one(comodel_name='delfisanggar.level', string='Kelas')
    
    session_ids = fields.One2many(comodel_name='delfisanggar.session', inverse_name='jadwal_tari_id', string='Session')
    