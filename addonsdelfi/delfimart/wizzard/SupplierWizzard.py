from odoo import api, fields, models


class Supplier(models.TransientModel):
    _name = 'delfimart.supplier'
    
    supplier_id = fields.Many2one(
        comodel_name='delfimart.pemasok', 
        string='New Supplier')

    nama_supplier = fields.Char(string='')
    

    def supplier_baru (self):
        for rec in self:
            self.env['delfimart.pemasok'].search([('id', '=', rec.supplier_id.id)]).write({'supplier': rec.nama_supplier})
        pass

    
    