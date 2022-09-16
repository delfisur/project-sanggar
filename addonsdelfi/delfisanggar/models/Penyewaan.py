from datetime import date
from datetime import datetime
from email.policy import default
from re import A
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Penyewaan(models.Model):
    _name = 'delfisanggar.penyewaan'
    _description = 'Penyewaan'
    _rec_name = 'kode'

    membership = fields.Boolean(string='Apakah peserta sanggar?')
    nama_non_peserta = fields.Char(string='Nama Nonpeserta')

    name = fields.Char(string='Name')
    kode = fields.Char(string='Kode Penyewaan', required=True, copy=False, readonly=True, default=lambda self:_('New'))
    user_id = fields.Many2one(comodel_name='res.partner', string='Nama Penyewa')
    # tgl_sewa = fields.Datetime(string='Tanggal Sewa', default=fields.Datetime.now())
    # tgl_limit = fields.Datetime(string='Tanggal Limit')

    tgl_sewa = fields.Date(string='Tanggal Sewa', default=fields.Date.today())
    tgl_limit = fields.Date(string='Tanggal Limit')
    tgl_skrg  = fields.Date(string='Tanggal Sekarang', default=fields.Date.today())

    dikembalikan_id = fields.Many2one(comodel_name='delfisanggar.pengembalian', string='Pengembalian')
    
    harga = fields.Integer(compute='_compute_harga', string='Harga/hari')
    hari = fields.Char(compute='_compute_hari',string='Total Hari')
    # hari = fields.Char(string='Total Hari Penyewaan')

    bayar = fields.Integer(compute='_compute_bayar',string='Total Pembayaran')

    

    jaminan = fields.Selection(string='Jaminan', selection=[('ktp', 'KTP'), ('uang', 'Rp.100.000')], required=True)
    
    list_ids = fields.One2many(comodel_name='delfisanggar.penyewaandetail', inverse_name='kode_id', string='List')

    state = fields.Selection(string='status', selection=[('formulir', 'Formulir'), ('sewakan', 'Acc Sewa'), ('cancel', 'Cancel')], required=True, readonly=True, default='formulir')
    
    sudah_kembali = fields.Boolean(string='Apakah sudah dikembalikan?', default=False)

            

    @api.depends('hari')
    def _compute_bayar(self):
        for record in self:
            if record.harga:
                record.bayar = record.harga * float(record.hari)
            else:
                record.bayar = 0


    @api.depends('tgl_sewa','tgl_limit')
    def _compute_hari(self):
        for i in self:
            if self.tgl_sewa and self.tgl_limit:
                i.hari = (i.tgl_limit - i.tgl_sewa).days
            else:
                i.hari = 0


    def action_formulir(self):
        for rec in self:
            rec.write({'state' : 'formulir'})

    def action_sewakan(self):
        for rec in self:
            rec.write({'state' : 'sewakan'})

    def action_cancel(self):
        for rec in self:
            rec.write({'state' : 'cancel'})


    @api.model
    def create(self, vals):
        if vals.get('kode', _('New')) == _('New'):
            vals['kode'] = self.env['ir.sequence'].next_by_code('delfisanggar.penyewaan') or _('New')
        record = super(Penyewaan,self).create(vals)
        return record

    @api.depends('list_ids')
    def _compute_harga(self):
        for record in self:
            x = sum(self.env['delfisanggar.penyewaandetail'].search([('kode_id', '=', record.id)]).mapped('sub_total'))
            record.harga = x

    @api.constrains('tgl_sewa','tgl_limit','tgl_skrg')
    def check_date(self):
        for rec in self:
            if rec.tgl_sewa > rec.tgl_limit:
                raise ValidationError ('Tanggal Penyewaan harus sebelum Tanggal Limit Pengembalian')
            elif rec.tgl_sewa < rec.tgl_skrg:
                raise ValidationError ('Tanggal tidak berlaku')





class Penyewaan_Details(models.Model):
    _name = 'delfisanggar.penyewaandetail'
    _description = 'List'

    kode_id = fields.Many2one(comodel_name='delfisanggar.penyewaan', string='kode')
    kostum_id = fields.Many2one(comodel_name='delfisanggar.kostum', string='Nama Kostum')
    hargasewa = fields.Integer(string='Harga Sewa')
    qty = fields.Integer(string='Qty')
    sub_total = fields.Integer(compute='_compute_harga', string='Harga/hari')
    
     
    @api.model
    def create(self, vals):
        record = super(Penyewaan_Details, self).create(vals)
        if record.qty:
            self.env['delfisanggar.kostum'].search([('id', '=', record.kostum_id.id)]).write({'stok': record.kostum_id.stok-record.qty})
            return record
        else:
            self.qty =''



    @api.onchange('kostum_id')
    def _onchange_harga(self):
        if (self.kostum_id.harga):
            self.hargasewa = self.kostum_id.harga
        else:
            self.hargasewa = ''


    @api.onchange('qty')
    def _compute_harga(self):
        for record in self:
            if record.qty:
                record.sub_total = record.qty * record.hargasewa
            else:
                record.sub_total = 0

    