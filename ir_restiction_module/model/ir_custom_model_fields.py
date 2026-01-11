from odoo import models, fields

class IrModelFields(models.Model):
    
    _inherit = "ir.model.fields"

    is_restricted = fields.Boolean(
        string="Restricted in Export",
        help="If enabled, this field will be hidden from the export dialog for non-admin users."
    )
    
    