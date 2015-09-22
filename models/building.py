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
    owner_ids = fields.One2many('res.partner','building_id', string='Owners')    
    rental_ids = fields.One2many('immo.rental','building_id', string='Rentals')