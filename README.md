# demo-shop

A tiny shopping cart (add items, discount codes, checkout with 9% GST), used to demo
`trace.py` from [group6-traceability](https://github.com/isis-eka/group6-traceability).
The user stories and their acceptance criteria are in `USER_STORIES.md`; the same criteria,
one per line, are in `criteria.txt`.

## Run the tests

```bash
pip install pytest
python -m pytest
```

## Run the traceability tool on it

From the `group6-traceability` folder (needs `OPENAI_API_KEY` in its `.env`):

```bash
python src/trace.py --repo ../demo-shop --criteria ../demo-shop/criteria.txt
```

One criterion only:

```bash
python src/trace.py --repo ../demo-shop --criterion "Given a cart with items, when the shopper checks out, then the receipt total is the subtotal plus 9% GST."
```

The report is written to `group6-traceability/reports/`.

**After editing any test**, delete `group6-traceability/workspace/_trace/demo-shop__local.index.jsonl`:
the tool caches the test index for a local folder and would otherwise search the old tests.
