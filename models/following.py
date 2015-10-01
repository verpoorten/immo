# -*- coding: utf-8 -*-

from openerp import models, fields
from datetime import timedelta

class Following(models.Model):
    _name = 'immo.following'
    _description = "following"
    _inherits = [['immo.revision','revision_id'],]
    
    following_state = fields.Selection([('A_VERIFIER', 'A vérifier'), ('PAYE', 'Payé'), ('IMPAYE', 'Impayé'), ('PAIEMENT_INCOMPLET', 'Paiement incomplet'), ('PAIEMENT_SUPERIEUR', 'Paiement supérieur')])
#     rent_expected = fields.Float(required=True)
    rent_paid = fields.Float(required=True)
    bank_account = fields.Char()
#     date_start = fields.Datetime()
#     date_end = fields.Datetime()
    payement_date = fields.Date()  
#     expected_payement_date = fields.Datetime()