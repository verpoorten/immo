# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
import datetime


class RevisionWizard(models.TransientModel):
    _name = 'immo.wizard.revision'
    
      
    rental_id = fields.Many2one('immo.rental', string='Rental')    
    revision_id = fields.Many2one('immo.revision', string='Revision')
    
    new_date = fields.Date()
    rent = fields.Float()
    charges = fields.Float()
    date_start = fields.Date()
    date_end = fields.Date()   
    date_end_rental = fields.Date()  
    date_start_old_revision = fields.Date() 
    date_end_old_revision = fields.Date() 
    
    @api.one
    def validate_revision(self):
        res_revision = self.env['immo.revision']
        
        existing_revisions = res_revision.search([('rental_id', '=', self.rental_id.id), ('id', '=', self.revision_id.id)])
        
        rev=None
        for result in existing_revisions:
            rev = result
        id_old_revision=rev.id    
        new_revision=res_revision.create({'rental_id':self.rental_id.id,'date_start':self.date_start,'date_end':self.date_end,'rent':self.rent,'charges':self.charges})
        rev.write({'date_end':self.date_start})
        res_following = self.env['immo.following']
        date_s= fields.Datetime.from_string(new_revision['date_start']) 
        existing_followings = res_following.search([('revision_id', '=', id_old_revision)]) 
       
        for result in existing_followings:
            ds= fields.Datetime.from_string(result['payement_date'])
            if ds >= fields.Datetime.from_string(new_revision['date_start']):
  
                result.write ({'following_state':'REVISION_LOYER','revision_id':new_revision.id})
            
        return True
    

    @api.constrains('date_start','date_end')
    def _check_date__end(self):
        for record in self:
            if record.date_start:
                if record.date_start_old_revision:
                    if fields.Datetime.from_string(record.date_start) < fields.Datetime.from_string(record.date_start_old_revision):
                        raise exceptions.ValidationError(_("La nouvelle date de début de la revision est inférieure à la date de début de l'ancienne révision"))                    
#                 if record.date_end_old_revision:    
                if record.date_end:
                    if fields.Datetime.from_string(record.date_start) > fields.Datetime.from_string(record.date_end):
                        raise exceptions.ValidationError(_("La nouvelle date de début de la revision est supérieure à la date de fin de la location"))
                    if fields.Datetime.from_string(record.date_start) > fields.Datetime.from_string(record.date_end_rental):
                        raise exceptions.ValidationError(_("La nouvelle date de début de la revision est supérieure à la date de fin de la location"))                    