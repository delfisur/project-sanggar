from odoo import models, fields, api


class Grup(models.Model):
    _name = 'delfimart.grup'
    _description = 'Grup Delfimart'
    # _rec_name = 'nomor_kode_grup'

   
        
    # name = fields.Char(
    #     string='Nama Grup')

    name = fields.Selection([
        ('makananbasah', 'Makanan Basah'),
        ('makanankering', 'Makanan Kering'),
        ('minuman', 'Minuman'),
        ('bahanmakanankering', 'Bahan Makanan Kering'),
        ('bahanmakananbasah', 'Bahan Makanan Basah')],
         string='Nama Grup', ondelete='cascade')

    # nomor_kode_grup = fields.Char(onchange='_onchange_namagrup',
    #     string='Kode Grup')

    nomor_kode_grup = fields.Char(
        string='Kode Grup')


    produk_ids = fields.One2many(
        comodel_name='delfimart.produk', 
        inverse_name='kode_grup_id', 
        string='Produk', ondelete='')

    # produk_id = fields.Many2one(
    #     comodel_name='delfimart.produk', 
    #     string='Produk')


#fungsi merubah:onchange
    @api.onchange('name')
    def _onchange_namagrup(self):
        if (self.name == 'makananbasah'):
            self.nomor_kode_grup = 'MKN135'
        elif (self.name == 'makanankering'):
            self.nomor_kode_grup ='MKN246'
        elif (self.name == 'minuman'):
            self.nomor_kode_grup = 'MNM01'
        elif (self.name == 'bahanmakanankering'):
            self.nomor_kode_grup = 'BHNMK246'
        elif (self.name == 'bahanmakananbasah'):
            self.nomor_kode_grup = 'BHNMK135'