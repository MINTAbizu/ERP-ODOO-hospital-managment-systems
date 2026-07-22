from odoo import api, fields,models


class speciallity(models.Model):
    _name='hospital.speciallity'
    description='doctor.s'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name='speciality'
       
       
employes= fields.Many2one("res.users", string="employee")
speciality=fields.Many2one("speciality.docotros"  ,string="specality")
speciality_lists=fields.Selection([("nurses","nurses"),("doctors","doctors"),("pharmacists","pharmacists"),('pediatric','pediatric')],string="speciality list")
taken_date=fields.Datetime(string="taken date",default=fields.Datetime.now())


