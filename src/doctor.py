"""Doctor module for validating the application tracker.

Provides utilities to check for invalid statuses or missing fields in the
tracker and report issues. Can be run as a script to perform a simple
health check of the tracker file.
"""
from typing import List

from .tracker import load_tracker, VALID_STATUSES, Application

def check_tracker(path: str = "tracker.json") -> List[str]:
    """
    Load the tracker and return a list of strings describing any issues
    found. If the list is empty, the tracker is considered healthy.

    :param path: Path to the tracker JSON file.
    :return: List of issue descriptions.
    """
    issues: List[str] = []
    applications = load_tracker(path)

    for app in applications:
        # Validate status
        if app.status not in VALID_STATUSES:
            issues.append(
                f"Application {app.id} ({app.title} at {app.company}) has invalid status '{app.status}'."
            )
        # Validate required fields
        if not app.title or not app.company:
            issues.append(
                f"Application {app.id} is missing a title or company name."
            )

    return issues


def main() -> None:
    """Entry point for running the doctor check from the command line."""
    issues = check_tracker()
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("Tracker is healthy. All applications have valid statuses and required fields.")


if __name__ == "__main__":  # pragma: no cover
    main()
