# -*- coding: utf-8 -*-
from openerp import models, fields, api

class RevisionWizard(models.TransientModel):
    _name = 'immo.wizard.revision'
    
    rental_id = fields.Many2one('immo.rental', string='Rental')
    revision_id = fields.Integer()
    new_date = fields.Datetime()
    rent = fields.Float()
    charges = fields.Float()
    date_start = fields.Datetime()  
    
    @api.one
    def validate_revision(self):
        res_revision = self.env['immo.revision']
        
#         existing_revisions = res_revision.search([('rental_id', '=', self.rental_id.id), ('revision_id', '=', self.revision_id.id)])
        existing_revisions = res_revision.search([('rental_id', '=', self.rental_id), ('revision_id', '=', self.revision_id)])
        rev=None
        for result in existing_revisions:
            rev = result
            
        new_revision=res_revision.create({'rental_id':self.rental_id,'date_start':self.date_start,'date_end':self.date_end,'rent':self.rent,'charges':self.charges})
        return True
    
