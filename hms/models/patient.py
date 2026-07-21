
from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient"
    

    name = fields.Char(string="Name", required=True, tracking=True)
    last_name=fields.Char(string="last_name" )
    dob = fields.Date(string="Date of Birth", required=True)
    address=fields.Char(string="address" )
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender",
        required=True,
    )

