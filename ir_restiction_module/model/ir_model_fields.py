from odoo import models, fields, api


class IrModelFields(models.Model):
    _inherit = 'ir.model.fields'

    is_restricted = fields.Boolean(string="Restricted")

    @api.model
    def get_fields_for_export(self, model):
        fields = self.search([
            ('model', '=', model),
            ('store', '=', True),
            ('exportable', '!=', False),
        ])
        return [
            {
                'id': field.name,
                'string': field.field_description,
                'name': field.name,
                'field_type': field.ttype,
                'is_restricted': field.is_restricted, 
            }
            for field in fields
        ]