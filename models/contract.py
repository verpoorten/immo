# -*- coding: utf-8 -*-

from openerp import models, fields

class Contract(models.Model):
    _name = 'immo.contract' 
    _inherits=[['immo.building','building_id'],]
    
    description = fields.Char()   
    contract_type = fields.Selection([('MANAGEMENT', 'Management')], required=True,default='MANAGEMENT')
    date_start = fields.Date(required=True)  
    date_end = fields.Date(required=True)
    policy_holder_id = fields.Many2one('res.partner',string="policy holder",required=True)
    executor_id = fields.Many2one('res.partner',string="executor",required=True)
