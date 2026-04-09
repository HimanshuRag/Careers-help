# Architecture and Roadmap

This project uses a JSON-first approach to store all structured data. Each evaluation produces two files:

- `reports/<id>.json`: machine-readable summary containing scores, grades and extracted fields.
- `reports/<id>.md`: human-readable report compiled from the JSON.

The tracker is stored in `tracker.json` to avoid brittle CSV/Markdown parsing. Each entry includes: `id`, `company`, `role`, `status`, `score`, `grade`, `archetype`, `remote`, `compensation` and `notes`.

## Modules

- **evaluation.py**: Contains `evaluate_job_description` which takes the text or URL of a job description and returns a structured JSON payload with scores and grades. You can customize the scoring logic here.
- **resume.py**: Plans how to adapt your resume based on the evaluation output. It does not generate the full resume but returns a structured plan.
- **cover_letter.py**: Provides a plan for a cover letter, including which accomplishments to highlight.
- **tracker.py**: Loads and saves the application tracker. It provides functions to add entries, update statuses and deduplicate offers.
- **cli.py**: CLI interface for running evaluations and updating the tracker.

## Roadmap

- Integrate portal scanners for major application platforms (Greenhouse, Workday, Lever).
- Add scheduler to remind you of follow-ups and deadlines.
- Build a web dashboard for live status tracking.
- Improve the evaluation engine by using LLMs via API for deeper semantic matching.
