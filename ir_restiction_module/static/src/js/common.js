/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ExportDataDialog } from "@web/views/export/export_data_dialog";

// ✅ Patch the component to override getExportedFields
patch(ExportDataDialog.prototype, {
    async getExportedFields(model, isCompatible, context = {}) {
        const fields = await this.orm.call("ir.model.fields", "get_fields_for_export", [model], {
            context,
        });

        // ✅ Filter out fields where is_restricted is true
        return fields.filter((f) => !f.is_restricted);
    },
});
