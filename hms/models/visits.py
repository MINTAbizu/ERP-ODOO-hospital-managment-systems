from odoo import  api ,fields,models


class patientvisits(models.Model):
    _name="patient.visits"
    _description="patient.visit.descrption"
    inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name='doctor_id'
    
    patient_id =fields.Many2one('hospital.patient', string="Visit", required=True )
    doctor_id=fields.Many2one("hospital.doctor", string="Visited by doctor" ,required=True)
    department_id= fields.Many2one("hr.department", string="department")
    date_of_visited= fields.Date(string="Date of Visited", default=fields.Datetime.now())
    visit_type=fields.Selection([ ("consultation","consultation"), ('follow_up',"follow_up"), ("emergency","emergency")])
    state=fields.Selection([("draft","draft"),("confirmed","confirmed"),("done","done"),("cancelled","cancelled")])
    chief_complaint= fields.Char(string="chief_complaint")
    diagnosis= fields.Char(string="diagnosis")
    treatment_plan= fields.Char(string="treatment_plan")
    notes= fields.Char(string="Note")
    