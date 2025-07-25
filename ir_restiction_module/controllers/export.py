from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.export import Export  # type: ignore

class ExportRestrictedController(Export):
    
    @http.route('/web/export/fields', type='json', auth="user")
    def export_fields(self, model, export_id):
        result = super().export_fields(model, export_id)

        if not request.env.user.has_group('base.group_system'):
            # Get all restricted fields for this model
            restricted_fields = request.env['ir.model.fields'].sudo().search([
                ('model', '=', model),
                ('is_restricted', '=', True)
            ])
            restricted_names = set(restricted_fields.mapped('name'))

            def filter_fields(fields):
                filtered = []
                for field in fields:
                    if field['name'] in restricted_names:
                        continue
                    if 'children' in field:
                        field['children'] = filter_fields(field['children'])
                    filtered.append(field)
                return filtered

            result = filter_fields(result)
        return result