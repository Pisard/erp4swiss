"""Make the Swiss QR slip page A4 (the swiss_accounting_software app draws it as US Letter).

"Create QR Bill" calls swiss_accounting_software.attach_pdf.attach_pdf, which hooks.py
redirects here (override_whitelisted_methods). We resize the uploaded slip page to A4 and
hand everything back to the original function, so the app itself is not modified.
"""

import base64
import io

import frappe
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

from swiss_accounting_software import attach_pdf as sas_attach_pdf

A4_WIDTH_PT = 595.276
A4_HEIGHT_PT = 841.890


@frappe.whitelist()
def attach_pdf(**kwargs):
	pdf_data = kwargs.get("pdf_data")
	if pdf_data and "," in pdf_data:
		header, encoded = pdf_data.split(",", 1)
		a4_pdf = to_a4(base64.b64decode(encoded))
		kwargs["pdf_data"] = header + "," + base64.b64encode(a4_pdf).decode("utf-8")

	return sas_attach_pdf.attach_pdf(**kwargs)


def to_a4(pdf_bytes):
	"""Set every page to A4. The slip is drawn from the bottom-left corner, so it keeps
	its exact size and stays at the bottom of the page; only empty margin changes."""
	reader = PdfReader(io.BytesIO(pdf_bytes))
	writer = PdfWriter()
	box = RectangleObject([0, 0, A4_WIDTH_PT, A4_HEIGHT_PT])

	for page in reader.pages:
		page.mediabox = box
		page.cropbox = box
		writer.add_page(page)

	output = io.BytesIO()
	writer.write(output)
	return output.getvalue()
