# -*- coding: utf-8 -*-

from openerp import models, fields

class Expense(models.Model):
    _name = 'immo.expense'        
    
    _inherits = [['immo.building','building_id'],]    
           
    description = fields.Char()  
    cost = fields.Float(required=True, default=0)