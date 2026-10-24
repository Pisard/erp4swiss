import frappe

# ERPNext queues every email and sends the queue only every 4 minutes (scheduler "all").
# Emails about a Sales Invoice are sent right away instead, in the background.
# If sending fails, the normal queue job retries it later as usual.

SEND_IMMEDIATELY_FOR = ("Sales Invoice",)


def send_immediately(doc, method=None):
	"""Email Queue after_insert: send invoice emails without waiting for the scheduler."""
	if doc.reference_doctype not in SEND_IMMEDIATELY_FOR:
		return
	if doc.status != "Not Sent" or doc.send_after:
		return

	frappe.enqueue(
		"erp4swiss.email_queue.send_queued_email",
		queue="short",
		enqueue_after_commit=True,
		name=doc.name,
	)


def send_queued_email(name: str):
	if not frappe.db.exists("Email Queue", name):
		return

	from frappe.email.doctype.email_queue.email_queue import EmailQueue

	# send() does nothing if emails are muted, the queue is suspended,
	# or the email was already picked up by the scheduler.
	EmailQueue.find(name).send()
