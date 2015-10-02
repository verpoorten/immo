# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    
    prenom = fields.Char()  
    buildings_ids = fields.Many2many('immo.building', relation='immo_owner_building', column1='owner_id', column2='building_id')
    rental_ids = fields.Many2many('immo.rental', relation='immo_tenant_rental', column1='tenant_id', column2='rental_id')

    contract_policy_holder_ids = fields.One2many('immo.contract','policy_holder_id', string='Policy holder')
    contract_executor_ids = fields.One2many('immo.contract','executor_id', string='Executor')
    guarantor_rental_ids = fields.Many2many('immo.rental', relation='immo_guarantor_rental', column1='guarantor_id', column2='rental_id')
#     guarantor_ids = fields.One2many('immo.rental','guarantor_id', string='Guarantor')
    
#     contract_executor_holder_ids = fields.One2many('immo.contract', 'executor_id',string='contracts')
    
    
    
   

    
