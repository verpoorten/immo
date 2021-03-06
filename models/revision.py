# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import timedelta

class Revision(models.Model):
    _name = 'immo.revision'
    _description = "revision"
    _inherits = [['immo.rental','rental_id'],]    
    _rec_name='rent'

    rent = fields.Float(required=True)
    charges = fields.Float(required=True)
    date_start = fields.Date()  
    date_end = fields.Date()
    rental_id = fields.Many2one('immo.rental', string='Rental',ondelete="restrict")
    following_ids = fields.One2many('immo.following','revision_id',string="Suivis")
    indice_sante = fields.Float()
    
    
    @api.multi
    def wizard_new_revision(self):
        wiz_id = self.env['immo.wizard.revision'].create({
            'rental_id': self.rental_id.id,
            'revision_id': self.id,
            'rent' :self.rent,
            'charges' :  self.charges,                    
            'date_end': self.date_end,
            'date_start_rental': self.rental_id.date_end,
            'date_end_rental': self.rental_id.date_end,
            'date_start_old_revision':self.date_start,
            'date_end_old_revision':self.date_end,
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'immo.wizard.revision',
            'res_id': wiz_id.id,
            'target': 'new',
        }
        
        
#         
#     def name_get(self,cr,uid,ids,context=None):
#         result = {}
#         for record in self.browse(cr,uid,ids,context=context):
#             result[record.id] = record.rent + ", " + record.charges
#     
#         return result.items()        