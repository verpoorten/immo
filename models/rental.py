# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from datetime import timedelta

class Rental(models.Model):
    _name = 'immo.rental'
    _description = "rental"
    _inherits = [['immo.building','building_id'],]    
    _rec_name='date_start'
    
    date_start = fields.Datetime(required=True)  
    date_end = fields.Datetime(required=True)  
    rent = fields.Float(required=True, default=500)
    charges = fields.Float(required=True, default=0)
    note = fields.Char()
    tenant_ids = fields.One2many('res.partner', 'rental_id',string='Tenants')
    revision_ids = fields.One2many('immo.revision', 'rental_id', string="Revision")
    

@api.constrains('date_start','date_end')
def _check_date_start_end(self):
    raise exceptions.ValidationError("Lavvvvv date de début est supérieure à la date de fin")
#     if self.date_start:
#         if self.date_end:
#             if fields.Datetime.from_string(self.date_start) > fields.Datetime.from_string(self.date_end):
#                 raise exceptions.ValidationError("La date de début est supérieure à la date de fin")
#             else:
#                 raise exceptions.ValidationError("Lavvvvv date de début est supérieure à la date de fin")

# @api.multi  
# def copy(self, default=None):
#     default=dict(default or {})
#     default['remarque']= "kkk"
# 
#     return super(Location,self).copy(default)
#      
#      
     
#     _sql_constraints = [
#                         ('remarque_unique',
#                         'UNIQUE(remarque)',"Il ne peut y avoir 2 fois la même remarque"),
#                         ]
#      
       
# def name_get(self,cr,uid,ids,context=None):
#     if not len(ids):
#         return []
#     res = [(r['id'],r['name'] and '%s [%s]' % (r['date_start'],r['date_end']) or r['name']) for r in self.read(cr,uid,ids,['date_start','date_end'],context= context)]
#     return res
# @api.multi  
# def create(self,default=None):
#     default=dict(default or {})
#     default_revision=dict(default or {})
#     default_revision['loyer']=self.loyer_initial
#     default_revision['location_id']=self.location_id
#     default['remarque']='test'
# #     Revision.create(default_revision)
#     super(Revision,self).create(default_revision)
#     return super(Location,self).create(default)
# 
# def create(self, cr, uid, vals, context=None):
#     default_revision=dict( {})
#     default_revision['loyer']=self.loyer_initial
#     default_revision['location_id']=self.location_id
#     att_id = self.pool.get('revision').create(cr,uid,{'loyer':500},context=context)
#     vals['remarque']='test'
#     res=super(location,self).create(cr,uid,vals,context=context)
#     return res

# @api.multi  
# def create(self, default=None):
#     default=dict(default or {})
# 
#     default['remarque']='test'
# 
#     return super(Location,self).create(default)

