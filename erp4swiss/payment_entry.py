import frappe

# ERPNext makes "Reference No" and "Reference Date" mandatory on Payment Entries
# against a bank account. ERP4Swiss makes them optional: when left empty,
# they are filled automatically before ERPNext validates the entry.


def fill_bank_reference(doc, method=None):
	"""Payment Entry before_validate."""
	if not doc.reference_no:
		doc.reference_no = doc.name
	if not doc.reference_date:
		doc.reference_date = doc.posting_date
