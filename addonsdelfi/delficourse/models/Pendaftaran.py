from odoo import fields, models, api


class Pendaftaran(models.Model):
    _name = 'delficourse.pendaftaran'
    _description = 'Pendaftaran Course'

    name = fields.Char(
        string='Jenis Kursus',
        required=False)

    pilihan = fields.Selection(selection=[('reguler', 'Reguler'), ('eksekutif', 'Eksekutif')],
                            string='Pilihan Kelas',
                            required=True)

    kapasitas_kelas = fields.Integer(
        string='Kapasitas Kelas',
        required=False)

    level_belajar = fields.Many2one(
        comodel_name='delficourse.level',
        string='Level Belajar',
        required=False)

    biaya = fields.Integer(compute='_compute_biaya',
        string='Biaya',
        required=False)

    @api.depends('level_belajar')
    def _compute_biaya(self):
        for i in self:
            i.biaya = i.level_belajar.biaya

    @api.depends('kapasitas_kelas')
    def _compute_sisa(self):
        for i in self:
            i.sisa_kapasitas = i.kapasitas_kelas



class Pemprograman(models.Model):
    _inherit = 'delficourse.pendaftaran'
    _name = 'delficourse.pemprograman'
    _description = 'ini kelas pemprograman'

    startup = fields.Char(
        string='Startup',
        required=False)
    
    jml_siswa_prog = fields.Integer(
        string='Jml Siswa Prog',
        required=False)

    sisa_kapasitas = fields.Integer(
        compute='_compute_sisa',
        string='Sisa Kapasitas',
        required=False)

    @api.depends('jml_siswa_prog')
    def _compute_sisa(self):
        for record in self:
            record.sisa_kapasitas = record.kapasitas_kelas - record.jml_siswa_prog


class Bahasa(models.Model):
    _inherit = 'delficourse.pendaftaran'
    _name = 'delficourse.bahasa'
    _description = 'ini kelas bahasa'
    materi = fields.Char(
        string='Materi',
        required=False)

    jml_siswa_bahasa = fields.Integer(
        string='Jml Siswa Bahasa',
        required=False)

    sisa_kapasitas = fields.Integer(
        compute='_compute_sisa',
        string='Sisa Kapasitas',
        required=False)

    @api.depends('jml_siswa_bahasa')
    def _compute_sisa(self):
        for record in self:
            record.sisa_kapasitas = record.kapasitas_kelas - record.jml_siswa_bahasa


class Keterampilan(models.Model):
    _inherit = 'delficourse.pendaftaran'
    _name = 'delficourse.keterampilan'
    _description = 'ini kelas keterampilan'
    seni = fields.Char(
        string='Seni', 
        required=False)

    jml_siswa_keterampilan = fields.Integer(
        string='Jml Siswa Keterampilan',
        required=False)

    sisa_kapasitas = fields.Integer(
        compute='_compute_sisa',
        string='Sisa Kapasitas',
        required=False)

    @api.depends('jml_siswa_keterampilan')
    def _compute_sisa(self):
        for record in self:
            record.sisa_kapasitas = record.kapasitas_kelas - record.jml_siswa_keterampilan

class Eskul(models.Model):
    _inherit = 'delficourse.pendaftaran'
    _name = 'delficourse.eskul'
    _description = 'ini kelas eskul'
    materi = fields.Char(
        string='Materi',
        required=False)

class Olahraga(models.Model):
    _inherit = 'delficourse.pendaftaran'
    _name = 'delficourse.olahraga'
    _description = 'ini kelas olahraga'
    bidang = fields.Char(
        string='Bidang',
        required=False)





