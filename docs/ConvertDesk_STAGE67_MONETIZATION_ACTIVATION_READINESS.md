# ConvertDesk Stage67 — Monetization Activation Readiness

## Purpose

Stage67 prepares ConvertDesk for real monetization activation after the public 1.0.2 release.

This stage does not put private secrets inside the desktop app.
This stage does not activate paid checkout.
This stage does not change the public 1.0.2 installer.

It creates the safe configuration files needed before Stage67.1:

- provider product checklist
- checkout-link config templates
- license-server environment template
- monetization readiness QA

## Product catalog to create

| Plan code | Product name | Billing | Launch price EUR | Feature plan |
|---|---|---:|---:|---|
| PRO_MONTHLY | ConvertDesk Pro Monthly | recurring monthly | 5.99 | PRO |
| PRO_YEARLY | ConvertDesk Pro Yearly | recurring yearly | 39.99 | PRO |
| PRO_LIFETIME | ConvertDesk Lifetime | one-time | 59.99 | PRO |
| BUSINESS_YEARLY | ConvertDesk Business Yearly | recurring yearly | 149.00 | BUSINESS |
| BUSINESS_LIFETIME | ConvertDesk Business Lifetime | one-time | 299.00 | BUSINESS |

## Recommended provider order

1. Paddle first
2. FastSpring backup
3. PayPro Global later

## Data needed before Stage67.1

Create the products in the chosen provider dashboard, then fill:

`config\checkout_links.live.json`

Required fields:

- `provider`
- `mode`
- `links.PRO_MONTHLY`
- `links.PRO_YEARLY`
- `links.PRO_LIFETIME`
- `links.BUSINESS_YEARLY`
- `links.BUSINESS_LIFETIME`
- `webhook_url`
- `license_server_url`

Do not put API keys or webhook secrets in the desktop app.

Private server secrets belong only in:

`license_server\.env`

## License server endpoint plan

Use the Stage62 server scaffold.

Public endpoints needed later:

- `POST /activate`
- `POST /validate`
- `POST /heartbeat`
- `POST /deactivate`
- `POST /webhook/paddle`
- `POST /webhook/fastspring`

## Stage67.1 will do later

After real checkout/product data exists:

1. validate checkout links
2. validate webhook URL
3. put live checkout links into website pricing/pro/business pages
4. connect desktop activation UI to hosted license server
5. run payment sandbox test
6. only then build 1.0.3 or 1.1.0
