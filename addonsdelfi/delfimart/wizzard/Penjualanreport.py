from odoo import fields, models, api


class PenjualanRepost(models.TransientModel):
    _name = 'delfimart.penjualanreport'
    _description = 'Description'

    pelanggan_id = fields.Many2one(
        comodel_name='delfimart.pelanggan',
        string='Pelanggan',
        required=False)

    dari_tgl = fields.Date(
        string='Dari Tanggal',
        required=False)

    ke_tgl = fields.Date(
        string='Ke Tanggal',
        required=False)

    def action_reportpenjualan(self):
        print(self.read()[0])
        member=[]
        pelanggan_id = self.pelanggan_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if pelanggan_id:
            member += [('pelanggan_id','=',pelanggan_id.id)]
        if dari_tgl:
            member += [('tgl_nota','>=',dari_tgl)]
        if ke_tgl:
            member += [('tgl_nota','<=',ke_tgl)]
        print(member)

        penjualan = self.env['delfimart.penjualan'].search_read(member)
        data = {
            'form': self.read()[0],
            'penjualan': penjualan
        }
        return self.env.ref('delfimart.report_penjualan_wizzardxx').report_action(self, data=data)
