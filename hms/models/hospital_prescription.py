from odoo import api ,fields,models


class hospital_prescription(models.Model):
    _name="hospital.prescription"
    _description="hospital prescription"
    
    patient_id=fields.Many2one("hospital.patient", string="patient", required=True)
    doctor_id=fields.Many2one("hospital.doctor", string="doctor" ,required=True)
    date= fields.date(string="date of prescption",required=True, default=fields.Datetime.now())
    notes=fields.Text(string="Notes")
    state = fields.Selection([("draft","Draft"),("confirmed","Confirmed"),("done","Done"),("cancelled","Cancelled")], default="draft", tracking=True)
    line_ids = fields.One2many("prescrption.line", "prescription_id", string="Prescription Lines")
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("reference", "New") == "New":
                vals["reference"] = self.env["ir.sequence"].next_by_code("hospital.prescription") or "PR/0000"
        return super().create(vals_list)
    
    
    
    
    def  confirm_action(self):
         self.state="confirmed"
         
    def  done_action(self):
         self.state="done"
         
    def   cancelle_action(self):
         self.state="cancelled"
         
         
         
class doctorprescrption_line(models.Model):
    _name="prescrption.line"
    _description="prescrption.line.descrption"
    
    
    prescription_id = fields.Many2one("hospital.prescription", string="Prescription", required=True, ondelete="cascade")
    product_id = fields.Many2one("product.product", string="Medicine")
    dosage = fields.Char(string="Dosage")
    frequency = fields.Char(string="Frequency")
    duration = fields.Char(string="Duration")
    instructions = fields.Text(string="Instructions")
    sequence = fields.Integer(string="Sequence", default=10)
    
    
    