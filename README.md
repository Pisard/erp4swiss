## ERP4Swiss

ERPNext customisations for Switzerland.

### What it contains

|Item|Where|What it does|
|-|-|-|
|Print Format `QR\_Sales\_Invoice`|`erp4swiss/erp4swiss/print\_format/qr\_sales\_invoice/`|French Sales Invoice (Facture) layout; address placed for a right-window envelope; prints `Reference` and `Concerne` when filled|
|Default print format|`erp4swiss/fixtures/property\_setter.json`|Sales Invoice prints with `QR\_Sales\_Invoice` by default|
|A4 QR slip|`erp4swiss/overrides/qr\_bill.py`|The QR slip page made by `swiss\_accounting\_software` is set to A4 (it is drawn as US Letter)|

### Requirements

* Frappe / ERPNext v16
* `swiss\_accounting\_software` installed on the site
* `Reference` / `Concerne` lines use Sales Invoice fields `reference` and `subject` (custom fields). If a site does not have them, those lines are simply not printed.

### Installation

```bash
cd \~/frappe-bench
bench get-app https://github.com/Pisard/erp4swiss.git --branch main
bench --site <site-name> install-app erp4swiss
bench restart
```

### Update

```bash
cd \~/frappe-bench/apps/erp4swiss \&\& git pull origin main
cd \~/frappe-bench \&\& bench --site <site-name> migrate
bench restart
```

### Changing the print format

`QR\_Sales\_Invoice` is a standard print format: change it in
`erp4swiss/erp4swiss/print\_format/qr\_sales\_invoice/qr\_sales\_invoice.json`
(update the `modified` timestamp to now), push, then run the update steps above.

### License

MIT

