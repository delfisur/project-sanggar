from odoo import fields, models, api


class SessionKeterampilan(models.Model):
    _name = 'delficourse.sessionketerampilan'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='delficourse.keterampilan',
        string='Nama Kursus',
        required=False)

    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Tutor',
        required=False,
        domain=[('function', '=', 'Tutor Keterampilan')])

    tgl_mulai = fields.Datetime(
        string='Tanggal Mulai',
        required=False,
        default=fields.Datetime.now())

    peserta_keterampilan_ids = fields.One2many(
        comodel_name='delficourse.pesertaketerampilan',
        inverse_name='session_id',
        string='Peserta_keterampilan_ids',
        required=False)

    jml_siswa = fields.Integer(
        compute='_compute_peserta',
        string='Jml Siswa',
        required=False)

    @api.model
    def _compute_peserta(self):
        for record in self:
            a = self.env['delficourse.pesertaketerampilan'].search([('session_id', '=', record.id)]).mapped('display_name')
            b = len(a)
            record.jml_siswa = b
            record.nama_kursus.jml_siswa_keterampilan = b

class PesertaKeterampilan(models.Model):
    _name = 'delficourse.pesertaketerampilan'
    _description = 'PesertaKeterampilan'

    name = fields.Char()
    peserta_id = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Keterampilan',
        required=False,
        domain=[('is_peserta', '=', True) and ('jenis_kursus', '=', 'keterampilan')])

    session_id = fields.Many2one(
        comodel_name='delficourse.sessionketerampilan',
        string='Session id',
        required=False)

