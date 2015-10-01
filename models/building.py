# -*- coding: utf-8 -*-

from openerp import models, fields

class Building(models.Model):
    _name = 'immo.building'    
    _description = "building"
    _rec_name='description'
    
       
    description = fields.Char()   
    street = fields.Char()
    number = fields.Char() 
    zip_code = fields.Char()
    city = fields.Char()
    country = fields.Char(default= "Belgium")
    
    owner_ids = fields.Many2many('res.partner', relation='immo_owner_building', column1='building_id', column2='owner_id')    
    rental_ids = fields.One2many('immo.rental','building_id', string='Rentals')
    expense_ids = fields.One2many('immo.expense','building_id', string='Expenses')
    contract_ids = fields.One2many('immo.contract','building_id', string='Contracts')     