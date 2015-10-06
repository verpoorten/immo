# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Building(models.Model):
    _name = 'immo.building'    
    _description = "building"
    _rec_name='description'
    _order = 'city'
       
    description = fields.Char()   
    street = fields.Char()
    number = fields.Char() 
    zip_code = fields.Char()
    city = fields.Char()
    country = fields.Char(default= "Belgium")
    
    peb = fields.Char()
    square_measure = fields.Float()
    precompte_immobilier = fields.Float()
    
    
    building_loan_bank_id = fields.Many2one('res.company',string ="Loan bank company")
    loan_total_amount = fields.Float()
    loan_buy_amount = fields.Float()
    loan_expenses_amount = fields.Float()
    loan_monthly_amount = fields.Float()
    load_start_date = fields.Date()
    load_end_date = fields.Date()
   
    
    owner_ids = fields.Many2many('res.partner', relation='immo_owner_building', column1='building_id', column2='owner_id')    
    rental_ids = fields.One2many('immo.rental','building_id', string='Rentals')
    expense_ids = fields.One2many('immo.expense','building_id', string='Expenses')
    contract_ids = fields.One2many('immo.contract','building_id', string='Contracts')     
    
    @api.multi
    @api.depends('description', 'street')
    def _name_get(self):
        result = []
        

        result.append((self.description, '%s (%s)' % (self.street, ', '.self.number)))
        return result