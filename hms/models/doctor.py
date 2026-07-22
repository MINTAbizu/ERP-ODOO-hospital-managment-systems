from odoo import api, fields,models


class hospitaldoctors(models.Model):
    _name='hospital.doctor'
    _description='doctor.descrption'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name='doctor_id'
    
    
    doctor_id=fields.Many2one("res.users", string="doctors", required=True , tracking=True)
    specialty_id =fields.Many2one("speciality.docotros"  ,string="specality")
    department_id= fields.Many2one("hr.department",string="Department")
    qualification= fields.Selection([('degree',"degree") ("masters","masters"),('specialized','specialized')])
    phone = fields.Char(string="Phone ")
    working_hours=fields.Char(string="Woring hour")
    

    

 