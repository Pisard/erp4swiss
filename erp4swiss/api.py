import frappe
from frappe import _

INVOICE_EMAIL_TEMPLATE = "Facture (ERP4Swiss)"


@frappe.whitelist()
def prepare_invoice_email(invoice: str) -> dict:
	"""Data for the "Envoyer par email" dialog of a submitted Sales Invoice.

	Returns the recipient, subject and message (from the Email Template) and the
	invoice PDF with the Swiss QR slip ({invoice}-QR.pdf). The QR PDF is created
	by swiss_accounting_software when it does not exist yet.
	"""
	doc = frappe.get_doc("Sales Invoice", invoice)
	doc.check_permission("read")

	if doc.docstatus != 1:
		frappe.throw(_("Please submit the Sales Invoice before sending it by email."))

	created = False
	qr_file = get_qr_pdf(doc.name)
	if not qr_file:
		from swiss_accounting_software.attach_pdf import attach_qr_bill

		attach_qr_bill(doc.name)
		qr_file = get_qr_pdf(doc.name)
		created = True

	if not qr_file:
		frappe.throw(_("The QR invoice PDF could not be created. Please click 'Create QR Bill' and try again."))

	email = get_invoice_email_text(doc)

	return {
		"recipients": get_customer_email(doc),
		"subject": email["subject"],
		"message": email["message"],
		"attachment": qr_file,
		"created": created,
	}


def get_qr_pdf(invoice: str) -> dict | None:
	"""Latest {invoice}-QR*.pdf attached to the invoice."""
	files = frappe.get_all(
		"File",
		filters={
			"attached_to_doctype": "Sales Invoice",
			"attached_to_name": invoice,
			"file_name": ["like", f"{invoice}-QR%.pdf"],
		},
		fields=["name", "file_name", "file_url", "file_size", "is_private"],
		order_by="creation desc",
		limit=1,
	)
	return files[0] if files else None


def get_customer_email(doc) -> str:
	"""Invoice contact email, else the customer's email, else its primary contact's email."""
	if doc.get("contact_email"):
		return doc.contact_email

	email = frappe.db.get_value("Customer", doc.customer, "email_id")
	if email:
		return email

	contacts = frappe.get_all(
		"Dynamic Link",
		filters={"link_doctype": "Customer", "link_name": doc.customer, "parenttype": "Contact"},
		pluck="parent",
	)
	for contact in contacts:
		email = frappe.db.get_value("Contact", contact, "email_id")
		if email:
			return email

	return ""


def get_invoice_email_text(doc) -> dict:
	"""Subject and message from the Email Template, with a French fallback."""
	if frappe.db.exists("Email Template", INVOICE_EMAIL_TEMPLATE):
		template = frappe.get_doc("Email Template", INVOICE_EMAIL_TEMPLATE)
		return template.get_formatted_email(doc.as_dict())

	return {
		"subject": _("Facture {0}").format(doc.name),
		"message": _("Bonjour,<br><br>Veuillez trouver ci-joint notre facture {0}.<br><br>Avec nos meilleures salutations,<br>{1}").format(
			doc.name, doc.company
		),
	}
