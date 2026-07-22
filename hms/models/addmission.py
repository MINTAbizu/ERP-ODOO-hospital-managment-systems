from  odoo import api ,fields,models
 
 
class  hospitalpatientaddmission(models.Model):
    _name="patient.addmission"
    _description="addmisson "
    
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name='patient_id'
    
    
    patient_id=fields.Many2one("hospital.patient" , string="patient", required=True)
    
    addmisiion=fields.Char(string="addmission")
    admission_date= fields.date(string="admission_date", default=fields.Datetime.now)
    
    bed_id= fields.Many2one("bed.management",string="bed")
    discharge_date=fields.date("Discharge date" , default=fields.Datetime.now())
    doctor_id=fields.Many2one("hospital.doctor", string="doctor", required=True)
    
    department=fields.Many2one("hr.department")
    
    state=fields.Selection([("draft","draft"),("admitted","admitted"),("discharged","discharged")])
    
    
    
    
    def action_drafted(self):
        self.state="draft"
    def action_admitted(self):
        self.state="admitted"
    def action_discharge(self):
        self.state="discharged"
    
    
    
 