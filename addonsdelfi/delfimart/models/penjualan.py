
from unicodedata import name
from odoo import models, fields, api

from odoo.exceptions import ValidationError


class Penjualan(models.Model):
    _name = 'delfimart.penjualan'
    _description = 'Penjualan'
    # _rec_name = 'user_id'

    membership = fields.Boolean(string='Apakah member')
    nama_nonmember = fields.Char(string='Nama')
    pelanggan_id = fields.Many2one (comodel_name='delfimart.pelanggan')
    id_member = fields.Char(compute='_compute_id_member', string='ID Member')


    name = fields.Char(
        string='No Nota')
    tgl_nota = fields.Datetime(
        string='Tgl Nota',
        default=fields.Datetime.now())

    # tgl_nota = fields.Char(
    #     string='Tgl Nota')

    total_bayar = fields.Integer(
        compute='_compute_total',
        string='Total Bayar')
    # kode_pelanggan_id = fields.Many2one(
    #     comodel_name='delfimart.pelanggan', 
    #     string='Kode Pelanggan')
    user_id = fields.Char(
        string='User ID')

    penjualandetail_ids = fields.One2many(
        # ondelete='_ondelete_penjualandetail',
        comodel_name='delfimart.penjualandetail', 
        inverse_name='no_nota_id', 
        string='Penjualan Detail')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
        string='Gender', required='True')

    state = fields.Selection(string='status', 
                            selection=[('draft', 'Draft'), ('confirm', 'Confirm'),('done','Done'),('cancel', 'Cancel')],
                            required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state' : 'confirm'})

    def action_done(self):
        self.write({'state' : 'done'})

    def action_cancel(self):
        self.write({'state' : 'cancel'})

    def action_draft(self):
        self.write({'state' : 'draft'})

    @api.depends('penjualandetail_ids')
    def _compute_total (self):
        for record in self:
            a = sum(self.env['delfimart.penjualandetail'].search([('no_nota_id', '=', record.id)]).mapped('sub_total'))
            record.total_bayar = a

    @api.depends('pelanggan_id')
    def _compute_id_member(self):
        for record in self:
            record.id_member = record.pelanggan_id.kode_pelanggan

    @api.onchange('pelanggan_id')
    def _onchage_pelanggan(self):
        if self.pelanggan_id.gender:
            self.gender = self.pelanggan_id.gender
        else:
            self.gender =''
    
    

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError ('Record yang bisa dihapus hanya draf')
        else:
            if self.penjualandetail_ids:
                a=[]
                for rec in self:
                    a = self.env['delfimart.penjualandetail'].search([('no_nota_id','=',rec.id)])
                    print (a)
                for i in a:
                    print(str(i.kode_barang_id.name)+ ' ' + str(i.jumlah))
                    i.kode_barang_id.stok += i.jumlah
            record = super(Penjualan, self).unlink()

    def write(self,vals):
        for rec in self:
            a = self.env['delfimart.penjualandetail'].search([('no_nota_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.kode_barang_id.name)+' '+str(data.jumlah)+' '+str(data.kode_barang_id.stok)) 
                data.kode_barang_id.stok += data.jumlah       
        record = super(Penjualan,self).write(vals)
        for rec in self:
            b = self.env['delfimart.penjualandetail'].search([('no_nota_id','=',rec.id)])
            print(a)
            print (b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.kode_barang_id.name)+' '+ str(databaru.jumlah)+' '+str(databaru.kode_barang_id.stok))
                    databaru.kode_barang_id.stok -= databaru.jumlah         
                else:
                    pass
        return record

    # (<nama constrains>,<implementasi>,<pesan eror)
    
    _sql_constraints = [
        ('no_nota_unik', 'unique(name)', 'No Nota harus unik ya..')
    ]


class Penjualan_Detail(models.Model):
    _name = 'delfimart.penjualandetail'
    _description = 'Penjualan Detail'

    no_nota_id = fields.Many2one(
        comodel_name='delfimart.penjualan', 
        string='No Nota')
    
    kode_barang_id = fields.Many2one(
        comodel_name='delfimart.barang', 
        string='Barang')

    # harga_jual = fields.Integer(
    #     # compute='_compute_hargasatuan',
    #     string='Harga Jual',
    #     related='kode_barang_id.harga_jual')

    harga_jual = fields.Integer(string='Harga Satuan')
    jumlah = fields.Integer(
        # compute=' _compute_qty',
        string='Jumlah')
    satuan = fields.Char(string='Satuan')

    sub_total = fields.Integer(
        compute='_compute_total',
        string='Sub Total')


    @api.onchange('kode_barang_id')
    def _onchange_harga_satuan(self):
        if (self.kode_barang_id.harga_jual):
            self.harga_jual = self.kode_barang_id.harga_jual
        else:
            self.harga_jual = ''

    @api.onchange('kode_barang_id')
    def _compute_satuan(self):
        self.satuan = self.kode_barang_id.satuan

    @api.depends('jumlah')
    def _compute_total(self):
        for record in self:
            if record.jumlah:
                record.sub_total = record.jumlah * record.harga_jual
            else:
                record.sub_total = 0
    
    @api.model
    def create(self, vals):
        record = super(Penjualan_Detail, self).create(vals)
        if record.jumlah:
            self.env['delfimart.barang'].search([('id', '=', record.kode_barang_id.id)]).write({
                'stok': record.kode_barang_id.stok-record.jumlah})
            return record
        else:
            self.jumlah =''

    @api.onchange('jumlah')
    def _compute_qty(self):
        for record in self:
            # self.env['delfimart.barang'].seacrh([('no_nota_id','=',rec.id)])
            if record.jumlah >= record.kode_barang_id.stok:
                record.jumlah == record.kode_barang_id.stok
            else:
                record.jumlah == ''

    @api.constrains('jumlah')
    def _checkquantity(self):
        for rec in self:
            if rec.jumlah < 1:
                raise ValidationError('Masukan jumlah belanjaan {} anda'.format(rec.kode_barang_id.name))
            elif rec.jumlah > rec.kode_barang_id.stok:
                raise ValidationError (f'Stok {rec.kode_barang_id.name} tidak mencukupi hanya tersedia {rec.kode_barang_id.stok} {rec.kode_barang_id.satuan}')