# -*- coding: utf-8 -*-

from openerp import models, fields

class Expense(models.Model):
    _name = 'immo.expense'        
    
    _inherits = [['immo.building','building_id'],]    
    date_start = fields.Date()  
    date_end = fields.Date()         
    description = fields.Char()  
    cost = fields.Float(required=True, default=0)