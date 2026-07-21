from odoo import models, fields, api


class PatientAppointment(models.Model):
    
    
    _name = "hospital.patient.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "reference"
    _rec_names_search = ["reference", "patient_id"]
    _description = "Patient Appointment"

    reference = fields.Char(
        string="Reference",
        default="NEW",
        readonly=True,
    )

    patient_id = fields.Many2one(
        "hospital.patient",
        string="Patient",
        required=True,
    )
    appoinetment_line_ids = fields.One2many(
        "hospital.patient.appointment_line",
        "appointment_id",
        string="Appointment Lines",
    )

    patientAppointment_date = fields.Date(
        string="Appointment Date",
        required=True,
    )

    Appintment_not = fields.Text(
        string="Appointment Note"
    )
    totalproduct_qty = fields.Float(
        compute="_compute_total_quantity",
        string="Total Quantity",
    )
    
    
    status_bar = fields.Selection([
    ('draft', 'Draft'),
    ('confirmed', 'Confirmed'),
    ('ongoing', 'Ongoing'),
    ('canceled', 'Canceled'),
    ('done', 'Done'),
    # ('paid', 'Paid'),
], default="draft", tracking=True)

    
    

    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            if vals.get("reference", "NEW") == "NEW":
                vals["reference"] = self.env["ir.sequence"].next_by_code(
                    "hospital.patient.appointment"
                )

        return super().create(vals_list)
    
    def _compute_total_quantity(self):
        for rec in self:
            total = sum(line.product_qty for line in rec.appoinetment_line_ids)
            rec.totalproduct_qty = total
            
    
    def action_confirem(self):
        for rec in self:
            rec.status_bar = "confirmed"
    
    def action_draft(self):
        for rec in self:
            rec.status_bar = "draft"
    
    def action_ongoing(self):
        for rec in self:
            rec.status_bar = "ongoing"
            
    # def action_cancel(self):
    #     for rec in self:
    #         rec.status_bar = ""
    
    def action_done(self):
        for rec in self:
            rec.status_bar = "done"
            
    # def action_cancels(self):
    #     self.status_bar = "canceled"
    
    # def action_paid(self):
    #     for rec in self:
    #         rec.status_bar='paid'
    
    
    
    
class PatientAppointment_line(models.Model):
    _name = "hospital.patient.appointment_line"
    _description = "Patient Appointment Line"

    appointment_id = fields.Many2one(
        "hospital.patient.appointment",
        string="Appointment",
        ondelete="cascade",
        required=True,
    )
    product_id = fields.Many2one(
        "product.product",
        string="Product",
    )
    product_qty = fields.Float(
        string="Quantity",
    )