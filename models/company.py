# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Company(models.Model):    
    _inherit = 'res.company'

    rental_owner_insurance_ids = fields.One2many('immo.rental','owner_insurance_company_id', string='Owner Insurance Company')
    rental_tenants_insurance_ids = fields.One2many('immo.rental','tenants_insurance_company_id', string='Tenant Insurance compay')
    building_loan_bank_ids = fields.One2many('immo.building','building_loan_bank_id',string ="Loan bank company")
    
    