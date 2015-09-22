# -*- coding: utf-8 -*-

from openerp import models, fields
from datetime import timedelta

class Revision(models.Model):
    _name = 'immo.revision'
    _description = "revision"
    _inherits = [['immo.rental','rental_id'],]    
    _rec_name='rent'

    rent = fields.Float(required=True)
    charges = fields.Float(required=True)
    date_start = fields.Datetime()  
    date_end = fields.Datetime()