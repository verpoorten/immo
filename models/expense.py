# -*- coding: utf-8 -*-

from openerp import models, fields

class Expense(models.Model):
    _name = 'immo.expense'            
    _inherits = [['immo.building','building_id'],] 
    _rec_name='description'
    
    date_start = fields.Date()  
    date_end = fields.Date()         
    description = fields.Char()  
    undertaker_id = fields.Many2one('res.partner',string="Undertaker",required=True)
    cost = fields.Float(required=True, default=0)
    expense_state = fields.Selection([('SOUHAIT', 'Souhait'), ('FAIT', 'Fait'), ('REFUSE', 'Refusé'), ('EN_COURS', 'En cours')])