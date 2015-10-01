# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'

#     rental_ids = fields.One2many('immo.rental','insurance_id', string='Insurance company')
    