from pyexpat import model
from odoo import models, fields, api

class Produk(models.Model):
    _name = 'delfimart.produk'
    _description = 'Ini produk delfimart'
    # _rec_name = 'nomor_kode_produk'

    nomor_kode_produk = fields.Char(string='Kode Produk')
    kode_spec = fields.Char(string='Kode Spec')
    name = fields.Selection([
        ('coklat', 'Coklat'),
        ('roti', 'Roti'),
        ('soda', 'Soda'),
        ('mie', 'Mie'),
        ('bihun', 'Bihun'),
        ('baso', 'Baso')],
         string='Nama Produk', ondelete='cascade')
    
    kode_grup_id = fields.Many2one(
        comodel_name='delfimart.grup', 
        string='Grup')

    barang_ids = fields.One2many(
        comodel_name='delfimart.barang', 
        inverse_name='kode_produk_id', 
        string='Barang')

    # produk_id = fields.Many2one(
    #     comodel_name='delfimart.produk', 
    #     string='Produk')

    # kode_produk_id = fields.Many2one(
    #     comodel_name='delfimart.produk', 
    #     string='Kode Produk')



    @api.onchange('name')
    def _onchange_namaproduk(self):
        if (self.name == 'coklat'):
            self.nomor_kode_produk = 'CKL'
        if (self.name == 'roti'):
            self.nomor_kode_produk = 'RT'
        if (self.name == 'soda'):
            self.nomor_kode_produk = 'SD'
        if (self.name == 'mie'):
            self.nomor_kode_produk = ' MIE'
        if (self.name == 'bihun'):
            self.nomor_kode_produk = 'BHN'
        if (self.name == 'baso'):
            self.nomor_kode_produk = 'BSO'
    
    #kodeproduk otomatis+kodespec

    @api.onchange('kode_grup_id','kode_spec')
    def _onchange_grup(self):
        if (self.kode_grup_id.nomor_kode_grup):
            self.nomor_kode_produk = str(self.kode_grup_id.nomor_kode_grup) +' '+ str(self.kode_spec)
        else:
            self.nomor_kode_produk =''