
from odoo import fields, models
# access_patienttag_user,patienttag_user,model_hospital.patient_tag,base.group_user,1,1,1,1

class HospitalPatient_tag(models.Model):
    _name = "hospital.patient_tag"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient_tag"
    

    name = fields.Char(string="Name", required=True, tracking=True)
    
