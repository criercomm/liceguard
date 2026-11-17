# LiceGuard landing page

One-page landing page for LiceGuard (Reese Consumer Health): "Non-Toxic Lice Treatment That Works on Super Lice." Built by Crier Communications from an SEO and AI-search visibility survey, November 2026.

Target address: https://www.liceguard.com/pages/non-toxic-lice-treatment (change the canonical and og:url lines in `src/template.html` if it lives elsewhere).

## Files

- `index.html`: the finished page, ready to publish. Product photos and logo are embedded, so it's a single file.
- `src/template.html`: the editable source. Images are placeholders like `{{ROBI}}`.
- `src/img/`: product photos and logo (WebP).
- `build.py`: rebuilds `index.html` from the source, embeds the images, and checks the structured data.

## Editing

Edit `src/template.html`, then run `python3 build.py`. Keep the visible FAQ answers and the FAQ answers in the JSON-LD block (in the page head) the same.

## Before launch

- Add the published clinical study for the Lice Repellent Hair Spray (24-hour claim) if Reese can share it.
- Name the retailers on the page if Reese provides a list (currently links to liceguard.com Where to Buy).
- On Shopify, the page can use LiceGuard's CDN image URLs in place of the embedded images.
