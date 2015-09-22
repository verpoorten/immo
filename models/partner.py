# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    _inherits = [['immo.building','building_id'],['immo.rental','rental_id'],]
    
    first_name = fields.Char()
    
