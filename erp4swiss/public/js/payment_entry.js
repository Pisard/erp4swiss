// ERP4Swiss: "Chèque/N° de Référence" and its date are optional on Payment Entry.
// Empty values are filled on save (reference = payment entry number, date = posting date).

const ERP4SWISS_OPTIONAL_FIELDS = ["reference_no", "reference_date"];

frappe.ui.form.on("Payment Entry", {
	setup(frm) {
		// ERPNext switches these two fields to mandatory when a bank account is selected.
		const toggle_reqd = frm.toggle_reqd.bind(frm);
		frm.toggle_reqd = function (fields, value) {
			const list = Array.isArray(fields) ? fields : [fields];
			const others = list.filter((f) => !ERP4SWISS_OPTIONAL_FIELDS.includes(f));
			const ours = list.filter((f) => ERP4SWISS_OPTIONAL_FIELDS.includes(f));
			if (ours.length) toggle_reqd(ours, 0);
			if (others.length) toggle_reqd(others, value);
		};
	},
});
