# -*- coding: utf-8 -*-
from openerp import models, fields, api

class RevisionWizard(models.TransientModel):
    _name = 'immo.wizard.revision'
    
      
    rental_id = fields.Many2one('immo.rental', string='Rental')    
    revision_id = fields.Many2one('immo.revision', string='Revision')
    
    new_date = fields.Date()
    rent = fields.Float()
    charges = fields.Float()
    date_start = fields.Date()
    date_end = fields.Date()    
    
    @api.one
    def validate_revision(self):
        res_revision = self.env['immo.revision']
        
#         existing_revisions = res_revision.search([('rental_id', '=', self.rental_id.id), ('revision_id', '=', self.revision_id.id)])AttributeError: 'int' object has no attribute 'id'
        #existing_revisions = res_revision.search([('rental_id', '=', self.rental_id.id), ('revision_id', '=', self.revision_id.id)])        
        existing_revisions = res_revision.search([('rental_id', '=', self.rental_id.id), ('id', '=', self.revision_id.id)])
        
        rev=None
        for result in existing_revisions:
            rev = result
            
        new_revision=res_revision.create({'rental_id':self.rental_id.id,'date_start':self.date_start,'date_end':self.date_end,'rent':self.rent,'charges':self.charges})
        rev.write({'date_end':self.date_start})
        return True
    
