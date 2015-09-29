# -*- coding: utf-8 -*-

from openerp import models, fields

class Contract(models.Model):
    _name = 'immo.contract' 
    _inherits=[['immo.building','building_id'],['res.partner','partner_id'],]
    
    description = fields.Char()   
    date_start = fields.Date(required=True)  
    date_end = fields.Date(required=True)
#     policy_holder_id = fields.Many2one('res.partner', string='Policy holder', ondelete="restrict")
#     executor_id = fields.Many2one('res.partner', string='Executor', ondelete="restrict")
#     building_ids = fields.One2many('immo.building', 'contract_id', string="Buildings")
#     executor_id = fields.Many2many('res.partner', relation='immo_policy_holder', column1='contract_id', column2='policy_holder_id')
#     student_ids = fields.Many2many('res.partner', domain="[('student', '=', 1)]", relation='epc_student_activityinfo', column1='activity_id', column2='student_id')