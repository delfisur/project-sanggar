from odoo import fields, models, api


class SessionPemprograman(models.Model):
    _name = 'delficourse.sessionpemprograman'
    _description = 'Description'

    name = fields.Char(string='Nama')
    nama_kursus = fields.Many2one(
        comodel_name='delficourse.pemprograman',
        string='Nama Kursus',
        required=False)

    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Tutor',
        required=False,
        domain=[('function', '=', 'Tutor Pemprograman')])

    tgl_mulai = fields.Datetime(
        string='Tanggal Mulai',
        required=False,
        default=fields.Datetime.now())

    peserta_pemprograman_ids = fields.One2many(
        comodel_name='delficourse.pesertapemprograman',
        inverse_name='session_id',
        string='Peserta_pemprograman_ids',
        required=False)

    jml_siswa = fields.Integer(
        compute='_compute_peserta',
        string='Jml Siswa',
        required=False)

    @api.model
    def _compute_peserta(self):
        for record in self:
            a = self.env['delficourse.pesertapemprograman'].search([('session_id', '=', record.id)]).mapped('display_name')
            b = len(a)
            record.jml_siswa = b
            record.nama_kursus.jml_siswa_prog = b

class PesertaPemprograman(models.Model):
    _name = 'delficourse.pesertapemprograman'
    _description = 'PesertaPemprograman'

    name = fields.Char()
    peserta_id = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Pemprograman',
        required=False,
        domain=[('is_peserta', '=', True) and ('jenis_kursus', '=', 'pemprograman')])

    session_id = fields.Many2one(
        comodel_name='delficourse.sessionpemprograman',
        string='Session id',
        required=False)

