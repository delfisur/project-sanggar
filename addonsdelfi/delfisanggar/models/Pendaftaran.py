from email.policy import default
from odoo import api, fields, models, _

class Pendaftaran(models.Model):
    _inherit = 'res.partner'
    _description = 'Registrasi'
    _rec_name = 'id_peserta'

    
    id_peserta = fields.Char(string='ID Peserta', required=True, copy=False, readonly=True, default=lambda self:_('New'))
    
    nisn = fields.Char(string='NISN')
    
    ttl = fields.Date(string='TTL')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('lakilaki', 'Laki-Laki'), ('perempuan', 'Perempuan')])
    
    status_pendidikan = fields.Char(string='Pendidikan')
    tingkatan_kelas = fields.Many2one(comodel_name='delfisanggar.level', string='Pilihan Kelas')
    
    # state = fields.Selection(string='status', selection=[('draf', 'Draf'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancel')], required=True, readonly=True, default='draft')
    
    @api.model
    def create(self, vals):
        if vals.get('id_peserta', _('New')) == _('New'):
            vals['id_peserta'] = self.env['ir.sequence'].next_by_code('delfisanggar.datamember') or _('New')
        record = super(Pendaftaran,self).create(vals)
        return record
    
    # def action_confirm(self):
    #     self.write({'state' : 'confirm'})

    # def action_done(self):
    #     self.write({'state' : 'done'})

    # def action_cancel(self):
    #     self.write({'state' : 'cancel'})

    # def action_draft(self):
    #     self.write({'state' : 'draft'})
    
