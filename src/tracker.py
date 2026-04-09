"""Application tracker module.

This module defines a simple application tracker data model and helper
functions to load, save, add, and update job applications. The tracker
operates on a JSON file (`tracker.json`) where each application is stored
as a dictionary.
"""
import json
from dataclasses import dataclass, asdict
from typing import List

# Define the canonical set of valid statuses for a job application
VALID_STATUSES = [
    "wishlist",
    "applied",
    "interviewing",
    "offered",
    "rejected",
    "withdrawn",
]

@dataclass
class Application:
    """Represents a job application entry in the tracker."""

    id: int
    title: str
    company: str
    status: str

    def __post_init__(self) -> None:
        if self.status not in VALID_STATUSES:
            raise ValueError(f"Invalid status '{self.status}'. Valid statuses: {', '.join(VALID_STATUSES)}")


def load_tracker(path: str = "tracker.json") -> List[Application]:
    """Load applications from a JSON file. Return an empty list if the file does not exist."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Application(**entry) for entry in data]
    except FileNotFoundError:
        return []


def save_tracker(applications: List[Application], path: str = "tracker.json") -> None:
    """Save the list of applications to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(app) for app in applications], f, indent=2)


def add_application(applications: List[Application], app: Application) -> None:
    """Add a new application to the tracker."""
    applications.append(app)


def update_application_status(applications: List[Application], app_id: int, new_status: str) -> None:
    """
    Update the status of an application by its id. Raises a ValueError if the
    application is not found or if the new status is invalid.
    """
    if new_status not in VALID_STATUSES:
        raise ValueError(f"Invalid status '{new_status}'. Valid statuses: {', '.join(VALID_STATUSES)}")

    for app in applications:
        if app.id == app_id:
            app.status = new_status
            return
    raise ValueError(f"Application with id {app_id} not found")
