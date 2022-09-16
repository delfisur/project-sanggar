from odoo import api, fields, models


class Session(models.Model):
    _name = 'delfisanggar.session'
    _description = 'Sesion Tari'

    absen = fields.Datetime(string='Kehadiran',required=True, default=fields.Datetime.now())
    user_id = fields.Many2one(comodel_name='res.partner', string='User ID')
    jadwal_tari_id = fields.Many2one(comodel_name='delfisanggar.jadwal', string='Jadwal Tari')
    # kelas_id = fields.Many2one(comodel_name='delfisanggar.level', string='Kelas')
    # materi_id = fields.Many2one(comodel_name='delfisanggar.materi', string='Materi')
    kelas = fields.Char(compute = '_compute_kelas', string='Kelas')
    materi = fields.Char(compute = '_compute_materi', string='Materi')
    
    @api.depends('jadwal_tari_id')
    def _compute_kelas(self):
        for record in self:
            record.kelas = record.jadwal_tari_id.kelas_id.name

    @api.depends('jadwal_tari_id')
    def _compute_materi(self):
        for record in self:
            record.materi = record.jadwal_tari_id.materi_id.name
    