# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import datetime


class Following(models.Model):
    _name = 'immo.following'
    _description = "following"
    _inherits = [['immo.revision','revision_id'],]
    _inherit = 'ir.needaction_mixin'
    _order = 'expected_payement_date'
    
    following_state = fields.Selection([('A_VERIFIER', 'A vérifier'), ('PAYE', 'Payé'), ('IMPAYE', 'Impayé'), ('PAIEMENT_INCOMPLET', 'Paiement incomplet'), ('PAIEMENT_SUPERIEUR', 'Paiement supérieur'),('REVISION_LOYER','Révision loyer')])
#     rent_expected = fields.Float(required=True)
    rent_paid = fields.Float(required=True)
    bank_account = fields.Char()
#     date_start = fields.Datetime()
#     date_end = fields.Datetime()
    payement_date = fields.Date()  
    expected_payement_date = fields.Date()  
    notes = fields.Char()
#     expected_payement_date = fields.Datetime()
    building_street = fields.Char(string='Building Street',
                               related='revision_id.rental_id.building_id.street')
    building_city = fields.Char(string='Building City',related='revision_id.rental_id.building_id.city')
    
    @api.model        
    def _needaction_domain_get(self): 
        d = date.today() + relativedelta(days=7)
#         Pourquoi ceci ne fonctionne pas???  
        #         d_plus_7   = date.today()+ relativedelta(days=7)
#         return [ ('following_state', '!=', 'PAYE'),('expected_payement_date','<',fields.Datetime.to_string(d_plus_7))]  
        return [ ('following_state', '!=', 'PAYE'),('expected_payement_date','<',d)]
        
#         return [ ('following_state', '!=', 'PAYE'),('expected_payement_date','<',(date.today() + datetime.timedelta(7)).strftime('%%Y-%%m-%%d') )]
#         return [('expected_payement_date','<',((date.today()-datetime.timedelta(days=10)).strftime('%Y-%m-%d')))]
# ne Fonctionne pas
#         d_moins_7 = date.today()- relativedelta(days=7)


#              
    
    @api.constrains('following_state','payement_date')
    def _check_date__end(self):
        for record in self:
            if record.following_state :
                if record.following_state == 'PAYE' :
                    if not record.payement_date :            
                        raise exceptions.ValidationError(_("Please encode a payement date"))
                           
