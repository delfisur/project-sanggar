from odoo import fields, models, api


class SessionBahasa(models.Model):
    _name = 'delficourse.sessionbahasa'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='delficourse.bahasa',
        string='Nama Kursus',
        required=False)

    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Tutor',
        required=False,
        domain=[('function', '=', 'Tutor Bahasa')])

    tgl_mulai = fields.Datetime(
        string='Tanggal Mulai',
        required=False,
        default=fields.Datetime.now())

    peserta_bahasa_ids = fields.One2many(
        comodel_name='delficourse.pesertabahasa',
        inverse_name='session_id',
        string='Peserta_bahasa_ids',
        required=False)

    jml_siswa = fields.Integer(
        compute='_compute_peserta',
        string='Jml Siswa',
        required=False)

    @api.model
    def _compute_peserta(self):
        for record in self:
            a = self.env['delficourse.pesertabahasa'].search([('session_id', '=', record.id)]).mapped('display_name')
            b = len(a)
            record.jml_siswa = b
            record.nama_kursus.jml_siswa_bahasa = b

class PesertaBahasa(models.Model):
    _name = 'delficourse.pesertabahasa'
    _description = 'PesertaBahasa'

    name = fields.Char()
    peserta_id = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Bahasa',
        required=False,
        domain=[('is_peserta', '=', True) and ('jenis_kursus', '=', 'bahasa')])

    session_id = fields.Many2one(
        comodel_name='delficourse.sessionbahasa',
        string='Session id',
        required=False)

