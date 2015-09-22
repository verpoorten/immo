# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    _inherits = [['immo.rental','rental_id'],]
    prenom = fields.Char()  
    buildings_ids = fields.Many2many('immo.building', relation='immo_owner_building', column1='owner_id', column2='building_id')
    rental_ids = fields.Many2many('immo.rental', relation='immo_tenant_rental', column1='tenant_id', column2='rental_id')

    
