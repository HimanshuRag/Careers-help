import os
import json
import pytest

# Import functions from the tracker module
from src.tracker import (
    VALID_STATUSES,
    load_tracker,
    save_tracker,
    add_application,
    update_application_status,
)


def test_valid_statuses():
    """Ensure the set of valid statuses includes expected values."""
    assert "Pending" in VALID_STATUSES
    assert "Applied" in VALID_STATUSES
    assert "Interviewing" in VALID_STATUSES
    assert "Offer" in VALID_STATUSES
    assert "Rejected" in VALID_STATUSES
    assert "Accepted" in VALID_STATUSES


def test_add_and_update_application(tmp_path):
    """Test adding an application and updating its status."""
    tracker_file = tmp_path / "tracker.json"

    # Initially, the tracker should be empty
    assert load_tracker(tracker_file) == []

    # Add a new application
    app = add_application(
        tracker_file,
        company="Acme Corp",
        role="Data Scientist",
        url="https://example.com/job/123",
        score=4.2,
        status="Pending",
        notes="Initial notes",
    )

    # After adding, the tracker should contain one entry
    tracker_data = load_tracker(tracker_file)
    assert len(tracker_data) == 1
    entry = tracker_data[0]
    assert entry["company"] == "Acme Corp"
    assert entry["status"] == "Pending"

    # Update the status of the application
    update_application_status(tracker_file, 0, "Applied")
    updated_data = load_tracker(tracker_file)
    assert updated_data[0]["status"] == "Applied"
