from datetime import date
from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'delfisanggar.pengembalian'
    _description = 'Pengembalian'

    kode_id = fields.Many2one(comodel_name='delfisanggar.penyewaan', string='Kode Sewa')
    
    name = fields.Char(string='Nama')
    
    cek_qty = fields.Integer(string='Cek Qty')

    tanggal_limit = fields.Date(compute='_compute_limit',string='Limit Tanggal')
    
    tgl_kembali = fields.Date(string='Tanggal Kembali', default=fields.Date.today())

    keterlambatan = fields.Char(compute='_compute_telat',string='Lewat deadline')
    # keterlambatan = fields.Char(string='Lewat deadline')

    denda = fields.Integer(compute='_compute_denda',string='Denda')
    # denda = fields.Integer(string='Denda')

    surat_penyewaan = fields.Boolean(string='Sesuaikan Kwitansi')

    kembali_jaminan = fields.Char(compute='_compute_jaminan',string='Kembalikan Jaminan')

    cek_barang = fields.Selection(string='Cek Barang', selection=[('sesuai', 'Sesuai'), ('tidak_sesuai', 'Tidak Sesuai')])
    qty_kembali = fields.Integer(string='Barang Kembali')

    penyewaan_ids = fields.One2many(comodel_name='delfisanggar.penyewaandetail', inverse_name='dikembalikan_id', string='List Barang')
    
    
    #ini ngembaliin stok logicnya blm nemu
    # def write(self,vals):
    #     for rec in self:
    #         a = self.env['delfimart.penyewaandetail'].search([('kostum_id','=',rec.id)])
    #         print(a)
    #         for data in a:
    #             data.kostum_id.stok += data.cek_qty       
    #     record = super(Pengembalian,self).write(vals)
    #     return record

    @api.depends('kembali_jaminan')
    def _compute_jaminan(self):
        for rec in self:
            rec.kembali_jaminan = rec.kode_id.jaminan_sewa


    @api.depends('tanggal_limit')
    def _compute_limit(self):
        for rec in self:
            rec.tanggal_limit = rec.kode_id.tgl_limit

    @api.model
    def create(self,vals):
        record = super(Pengembalian, self).create(vals)
        if record.surat_penyewaan == True:
            self.env['delfisanggar.penyewaan'].search([('id','=', record.kode_id.id)]).write({'sudah_kembali':True})
            return record
    
    
    # @api.multi
    @api.depends('tanggal_limit','tgl_kembali')
    def _compute_telat(self):
        for i in self:
            if self.tanggal_limit and self.tgl_kembali:
                i.keterlambatan = (i.tgl_kembali - i.tanggal_limit).days
            else:
                i.keterlambatan = 0

    # @api.multi
    @api.depends('keterlambatan')
    def _compute_denda (self):
        for record in self:
            if float(record.keterlambatan) <= 0:
                record.denda = 0.0
            elif float(record.keterlambatan) >= 1:
                record.denda = 10000* float(record.keterlambatan)
            elif float(record.keterlambatan) >= 5:
                record.denda = 20000* float(record.keterlambatan)
            
   

