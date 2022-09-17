from odoo import fields, models, api

class BarangDatang(models.TransientModel):
    _name = 'delfimart.barangdatang'

    barang_id = fields.Many2one(
        comodel_name='delfimart.barang',
        string='Nama Barang',
        required=True)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def barang_datang (self):
        for rec in self:
            self.env['delfimart.barang'].search([('id', '=', rec.barang_id.id)]).write({'stok': rec.barang_id.stok + rec.jumlah})
        pass
    
