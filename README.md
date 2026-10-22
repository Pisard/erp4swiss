## ERP4Swiss

ERPNext customisations for Switzerland.

### What it contains

| Item | Where | What it does |
|---|---|---|
| Print Format `QR_Sales_Invoice` | `erp4swiss/erp4swiss/print_format/qr_sales_invoice/` | French Sales Invoice (Facture) layout; address placed for a right-window envelope; prints `Reference` and `Concerne` when filled |
| Default print format | `erp4swiss/fixtures/property_setter.json` | Sales Invoice prints with `QR_Sales_Invoice` by default |
| Reference / Concerne fields | `erp4swiss/fixtures/custom_field.json` | Adds `Reference` and `Subject` to Sales Invoice (section "Reference Information") |
| A4 QR slip | `erp4swiss/overrides/qr_bill.py` | The QR slip page made by `swiss_accounting_software` is set to A4 (it is drawn as US Letter) |

### Requirements

- Frappe / ERPNext v16
- `swiss_accounting_software` installed on the site
- `Reference` and `Subject` fields on Sales Invoice are created by this app

### Installation

```bash
cd ~/frappe-bench
bench get-app https://github.com/Pisard/erp4swiss.git --branch main
bench --site <site-name> install-app erp4swiss
bench restart
```

### Update

```bash
cd ~/frappe-bench/apps/erp4swiss && git pull origin main
cd ~/frappe-bench && bench --site <site-name> migrate
bench restart
```

### Changing the print format

`QR_Sales_Invoice` is a standard print format: change it in
`erp4swiss/erp4swiss/print_format/qr_sales_invoice/qr_sales_invoice.json`
(update the `modified` timestamp to now), push, then run the update steps above.

### License

MIT
