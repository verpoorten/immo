# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import datetime
import contextlib



class Rental(models.Model):
    _name = 'immo.rental'
    _description = "rental"
    _inherits = [['immo.building','building_id'],]    
#     _rec_name='date_start'
    
    contract_date = fields.Date()  
    date_start = fields.Date(required=True)  
    date_end = fields.Date(required=True)  
    rent = fields.Float(required=True, default=500)
    charges = fields.Float(required=True, default=0)
    note = fields.Char()    
    tenant_ids = fields.Many2many('res.partner', relation='immo_tenant_rental', column1='rental_id', column2='tenant_id')
    revision_ids = fields.One2many('immo.revision', 'rental_id', string="Revision")
    indice_sante_initial = fields.Float()
    guarantor_ids = fields.Many2many('res.partner', relation='immo_guarantor_rental', column1='rental_id', column2='guarantor_id')
    owner_insurance_company_id = fields.Many2one('res.company',string ="Owner insurance company")
    tenants_insurance_company_id = fields.Many2one('res.company',string ="Tenants insurance company")    
    attachments = fields.Many2many('ir.attachment', string="Attachments")
    
    @api.onchange('date_start')
    def _verify_dates(self):
        if self.date_start and not self.date_end:            
            self.date_end = fields.Datetime.to_string(fields.Datetime.from_string(self.date_start) + relativedelta(years=3))
            
    @api.one
    def copy(self, default=None):
        default = dict(default or {})
        default['date_start'] =self.date_end
        return super(Rental, self).copy(default)
    
    @api.model
    def create(self,values):
        new_rental = super(Rental,self).create(values)
        rev=dict({})
        rev['rent'] = new_rental.rent
        rev['charges'] = new_rental.charges

        rev['rental_id'] = new_rental.id 
        rev['date_start'] = new_rental.date_start
        rev['date_end'] = new_rental.date_end
 
        new_rev=self.env['immo.revision'].create(rev)
        date_fin = fields.Datetime.from_string(new_rev.date_end) 
        date_d = fields.Datetime.from_string(new_rev.date_start) 
        date_f = fields.Datetime.from_string(new_rev.date_start) + relativedelta(months=1)
        i=0
        while date_f <= date_fin:
            res_fol = self.env['immo.following']      
            fol=dict({})
            fol['revision_id'] = new_rev.id 
            fol['following_state'] = 'A_VERIFIER'
            fol['expected_payement_date'] =fields.Datetime.to_string(date_d)
            fol['rent_paid'] = new_rental.rent 
            res_fol.create(fol)
            
            date_d = date_d + relativedelta(months=1)
            date_f = date_f + relativedelta(months=1)
            i=i+1

        return new_rental

    
    
    

    @api.constrains('date_start','date_end')
    def _check_date_start_end(self):
        for record in self:
            if record.date_start:
                if record.date_end:
                    if fields.Datetime.from_string(record.date_start) > fields.Datetime.from_string(record.date_end):
                        raise exceptions.ValidationError("La date de début est supérieure à la date de fin")
                    

    def name_get(self,cr,uid,ids,context=None):
        result = {}
        for record in self.browse(cr,uid,ids,context=context):
            result[record.id] = str(record.date_start) + " au " + str(record.date_end)
    
        return result.items()
