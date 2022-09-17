from odoo import models, fields, api

class Barang(models.Model):
    _name = "delfimart.barang"
    _description = "Barang barangnya"
    # _rec_name = 'nama_barang'

    kode_spec = fields.Char(string='Kode Spec')
    
    kode_barang = fields.Char(
        string='Kode Barang')

    kode_produk_id = fields.Many2one(
        comodel_name='delfimart.produk', 
        string='Kode Produk')
        
    name = fields.Char(
        string='Nama Barang')
    satuan = fields.Char(
        string='Satuan')
    harga_beli = fields.Integer(
        string='Harga Satuan')
    harga_jual = fields.Integer(
        compute = '_compute_hargajual',
        string='Harga Jual')
    stok = fields.Integer(
        string='Stok')

    supplier_ids = fields.Many2many(comodel_name='delfimart.pemasok', string='Daftar Supplier')
    
    #  harga_beli = fields.Integer(
    #     compute='_compute_hargasatuan',
    #     string='Harga Satuan')

    # barang_ids = fields.One2many(
    #     comodel_name='delfimart.grup', 
    #     inverse_name='', 
    #     string='')

    # @api.depends()
    # def _compute_hargasatuan(self):
    #     for record in self:
    #         record.harga_beli = record.kode_barang_id.harga_beli

    @api.depends('harga_beli')
    def _compute_hargajual(self):
        for record in self:
            if record.harga_beli:
                record.harga_jual = record.harga_beli + (record.harga_beli * (20/100))
            else:
                record.harga_jual = 0

    @api.onchange('kode_produk_id','kode_spec')
    def _onchange_produk(self):
        self.kode_barang = str(self.kode_produk_id.nomor_kode_produk) + ' ' + str(self.kode_spec)

       

