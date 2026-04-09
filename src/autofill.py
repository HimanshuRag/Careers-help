"""
autofill.py - experimental auto-fill for job applications using Playwright.

This module provides helper functions to automatically fill common fields on job
application forms. It does not submit the form automatically—you should review
and submit manually after automation.

Requires Playwright. Install with:
    pip install playwright
    playwright install chromium
"""

import asyncio
from dataclasses import dataclass
from typing import Optional, Dict

try:
    from playwright.async_api import async_playwright  # type: ignore
except ImportError:
    async_playwright = None  # Playwright is an optional dependency


@dataclass
class ApplicantProfile:
    """Data about the applicant used to pre-fill job application forms."""
    first_name: str
    last_name: str
    email: str
    phone: str
    resume_path: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


async def _fill_common_fields(page, profile: ApplicantProfile) -> None:
    """Attempt to fill common form fields on the current page."""
    selectors: Dict[str, list[str]] = {
        "first_name": [
            'input[name="firstName"]',
            'input[name="first_name"]',
            'input[name="firstname"]',
        ],
        "last_name": [
            'input[name="lastName"]',
            'input[name="last_name"]',
            'input[name="lastname"]',
        ],
        "email": [
            'input[type="email"]',
            'input[name="email"]',
        ],
        "phone": [
            'input[type="tel"]',
            'input[name="phone"]',
            'input[name="phoneNumber"]',
        ],
        "address": [
            'input[name="address"]',
            'input[name="street"]',
        ],
        "city": ['input[name="city"]'],
        "state": ['input[name="state"]'],
        "zip_code": [
            'input[name="zip"]',
            'input[name="postal"]',
        ],
    }

    for field, sel_list in selectors.items():
        value = getattr(profile, field)
        if not value:
            continue
        for sel in sel_list:
            locator = page.locator(sel)
            if await locator.count() > 0:
                await locator.first.fill(value)
                break

    # Upload resume file if possible
    if profile.resume_path:
        file_input = page.locator('input[type="file"]')
        if await file_input.count() > 0:
            await file_input.set_input_files(profile.resume_path)


async def auto_fill_application(
    url: str,
    profile: ApplicantProfile,
    additional_fields: Optional[Dict[str, str]] = None,
    headless: bool = True,
):
    """
    Open the job application URL in a browser, fill common fields using the
    provided ApplicantProfile, and optionally fill extra fields by selector.

    This function does not submit the form automatically. Review the page and
    click the submit button manually after verifying all information.
    """
    if async_playwright is None:
        raise RuntimeError(
            "Playwright is not installed. Run `pip install playwright` and"
            " `playwright install chromium` first."
        )
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        # Wait for the DOM content to load
        await page.wait_for_load_state("domcontentloaded")
        await _fill_common_fields(page, profile)

        # Fill any additional custom fields specified by selector
        if additional_fields:
            for selector, value in additional_fields.items():
                locator = page.locator(selector)
                if await locator.count() > 0:
                    await locator.first.fill(value)

        # Return the page object so the caller can review or submit
        return page


def fill_application(
    url: str,
    profile: ApplicantProfile,
    additional_fields: Optional[Dict[str, str]] = None,
    headless: bool = True,
):
    """Synchronous wrapper around auto_fill_application."""
    return asyncio.run(
        auto_fill_application(
            url=url,
            profile=profile,
            additional_fields=additional_fields,
            headless=headless,
        )
    )
