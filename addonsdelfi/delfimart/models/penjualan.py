
from odoo import models, fields, api


class Penjualan(models.Model):
    _name = 'delfimart.penjualan'
    _description = 'Penjualan'
    _rec_name = 'kode_pelanggan_id'

    no_nota = fields.Char(
        string='No Nota')
    tgl_nota = fields.Datetime(
        string='Tgl Nota',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        compute='_compute_total',
        string='Total Bayar')
    kode_pelanggan_id = fields.Many2one(
        comodel_name='delfimart.pelanggan', 
        string='Kode Pelanggan')
    user_id = fields.Char(
        string='User ID')

    penjualandetail_ids = fields.One2many(
        comodel_name='delfimart.penjualandetail', 
        inverse_name='no_nota_id', 
        string='Penjualan Detail')

    @api.depends('penjualandetail_ids')
    def _compute_total (self):
        for record in self:
            a = sum(self.env['delfimart.penjualandetail'].search([('no_nota_id', '=', record.id)]).mapped('sub_total'))
            record.total_bayar = a

class Penjualan_Detail(models.Model):
    _name = 'delfimart.penjualandetail'
    _description = 'Penjualan Detail'

    no_nota_id = fields.Many2one(
        comodel_name='delfimart.penjualan', 
        string='No Nota')
    
    kode_barang_id = fields.Many2one(
        comodel_name='delfimart.barang', 
        string='Barang')

    harga_jual = fields.Integer(
        # compute='_compute_hargasatuan',
        string='Harga Jual',
        related='kode_barang_id.harga_jual')

    jumlah = fields.Integer(
        string='Jumlah')

    sub_total = fields.Integer(
        compute='_compute_total',
        string='Sub Total')


    @api.depends('jumlah')
    def _compute_total(self):
        for record in self:
            if record.jumlah:
                record.sub_total = record.jumlah * record.harga_jual
            else:
                record.sub_total = 0

    
    

