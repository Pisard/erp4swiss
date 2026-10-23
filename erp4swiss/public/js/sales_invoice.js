// ERP4Swiss: "Envoyer par email" on submitted Sales Invoices.
// Opens ERPNext's email window pre-filled with the customer email, the French
// email template and the invoice PDF with the Swiss QR slip as attachment.

frappe.ui.form.on("Sales Invoice", {
	refresh(frm) {
		if (frm.doc.docstatus !== 1) return;

		frm.add_custom_button(__("Envoyer par email"), () => erp4swiss_send_invoice_email(frm));
	},
});

function erp4swiss_send_invoice_email(frm) {
	frappe.call({
		method: "erp4swiss.api.prepare_invoice_email",
		args: { invoice: frm.doc.name },
		freeze: true,
		freeze_message: __("Préparation de l'email..."),
		callback(r) {
			const data = r.message;
			if (!data) return;

			new frappe.views.CommunicationComposer({
				frm: frm,
				doc: frm.doc,
				title: __("Envoyer la facture {0}", [frm.doc.name]),
				recipients: data.recipients,
				subject: data.subject,
				message: data.message,
				attach_document_print: false,
				attachments: [data.attachment],
				selected_attachments: new Set([data.attachment.name]),
			});

			if (data.created) {
				frm.reload_doc();
			}
		},
	});
}
