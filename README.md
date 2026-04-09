# Job Ops Pro

Job Ops Pro is a structured, JSON-first job application pipeline. It evaluates job descriptions across multiple dimensions, plans resume and cover letter updates, deduplicates offers and tracks application status. It is a cleaned and improved version of the original Career-Ops system.

## Features

- **Structured evaluation**: Evaluate offers across dimensions such as role match, skills alignment, seniority stretch and compensation. Returns a JSON payload with scores and grades.
- **Resume plan generator**: Extract keywords from the job description and plan how to adapt your CV for each application.
- **Cover letter plan**: Generate a structured outline for a personalized cover letter.
- **Duplicate detection**: Avoid re-applying to the same job by checking application IDs.
- **Canonical statuses**: Track offers through consistent states (new, reviewed, applied, rejected, interviewing, offer, archived).
- **Doctor command**: Validate your installation, configuration and data.
- **CLI entry points**: Run evaluations, plan resumes or cover letters, update the tracker and more.
- - **Autofill application forms**: Use Playwright to automatically fill job application forms with your profile data (name, email, phone, etc.), including resume uploads and custom selectors, leaving submission for manual review.


## Installation

Use pip to install the dependencies:

    pip install -r requirements.txt

## Usage

Run the CLI for a job description:

    python -m src.cli evaluate --jd "<job description here>" --id "<id>" --company "<company>" --role "<role>"

See `docs/architecture.md` for more details and a roadmap.
