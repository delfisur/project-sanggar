from unicodedata import name
from odoo import api, fields, models


class Kostum(models.Model):
    _name = 'delfisanggar.kostum'
    _description = 'New Description'

    kode_kostum = fields.Char(string='Kode Kostum')
    name = fields.Char(string='Nama Kostum')
    deskripsi = fields.Char(string='Isi Kostum')
    
    stok = fields.Integer(string='Stok')
    sisa_stok = fields.Integer(string='Sisa Stok')
    status_penyewaan = fields.Char(string='Status Penyewaan')

    image_kostum = fields.Binary(string='Kostum Image', max_width=10, max_height=10)
    harga = fields.Integer(string='Harga')

    harga_nonpeserta = fields.Integer(compute='_compute_harga_nonpeserta',string='Harga Non Peserta')
    

    @api.depends('harga')
    def _compute_harga_nonpeserta(self):
        for record in self:
            if record.harga:
                record.harga_nonpeserta = record.harga + (record.harga * (20/100))
            else:
                record.harga_nonpeserta = 0
    

class AlatMusik(models.Model):
    _inherit = 'product.product'
    _description = 'Produk & Jasa'

    name = fields.Char()

