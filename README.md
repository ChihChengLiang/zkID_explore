# zkID_explore

Diverse-seed discovery of zkID / selective-disclosure use cases (Taiwan focus). See [docs/design.md](docs/design.md) for the pipeline, arms, critic prompt and metrics.

- `zkID_Taiwan_MyData_Use_Cases.xlsx` - prior workbook: rubric, 15-row matrix, Discovery Matrix.
- `sources/` + `schema/source.schema.json` - corpora to mine (batch 001: 20 in-domain sources).
- `seeds/` + `schema/seed.schema.json` - extracted, evidence-verified (problem, mechanism, domain, source, evidence) seeds; the unit agents are fed.
- `config/domains.yaml` - domain groups for distance enforcement.

```bash
python3 scripts/validate.py            # validate sources
python3 scripts/check_urls.py --write  # record reachability
```
