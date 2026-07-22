
from odoo import api, fields, models


class bedmanagement(models.Model):
    _name="bed.management"
    
    _description="bed management "
    inherit = ["mail.thread", "mail.activity.mixin"]
    # _rec_name='patient_id'
    
    patient_id=fields.Many2one("hospital.patient" ,string="patient")
    name= fields.Char(string="bed name")
    bed_capacity= fields.Char(string="capacity")
    
    ward_id= fields.Many2one("hospital.doctor",string="ward assigned doctor")
    
    location_bed=fields.Char(string="bed location")
    bed_type= fields.Selection([("single","single"),("double","double"),("vip","Vip")])
    bed_status=fields.Selection([("freee","free"),("occupied","occupied")  ,("maintenance","maintenance")])
    
    
    