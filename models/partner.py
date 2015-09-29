# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
#     _inherits = [['immo.rental','rental_id'],['immo.contract','contract_id'],]
    _inherits = [['immo.rental','rental_id'],]
    
    prenom = fields.Char()  
    buildings_ids = fields.Many2many('immo.building', relation='immo_owner_building', column1='owner_id', column2='building_id')
    rental_ids = fields.Many2many('immo.rental', relation='immo_tenant_rental', column1='tenant_id', column2='rental_id')
#     contract_policy_holder_ids = fields.Many2many('immo.contract', relation='immo_policy_holder_contract', column1='policy_holder_id', column2='contract_id')
#     contract_executor_ids = fields.Many2many('immo.contract', relation='immo_executor_contract', column1='executor_id', column2='contract_id')
#     contract_policy_holder_ids = fields.One2many('immo.contract', 'partner_id',string='contracts')
    contract_policy_holder_ids = fields.One2many('immo.contract','policy_holder_id', string='Policy holder')
    contract_executor_ids = fields.One2many('immo.contract','executor_id', string='Executor')
    
#     contract_executor_holder_ids = fields.One2many('immo.contract', 'executor_id',string='contracts')

    
    
   

    
