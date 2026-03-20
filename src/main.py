"""Minimal data collector."""

import asyncio
from pathlib import Path

import zendriver as zd
from zendriver import cdp


async def handler(event: object, tab: zd.Tab) -> None:
    """Handle CDP events and manage pending requests."""
    if not isinstance(event, cdp.network.RequestWillBeSent):
        return

    headers = event.request.headers

    if "accept" not in headers:
        return

    if headers["accept"] != "application/json":
        return

    await asyncio.sleep(2)

    body, _ = await tab.send(
        cdp.network.get_response_body(
            request_id=event.request_id
        )
    )

    print("─ Scraped XHR request ────────────────────────────")
    print(body)
    print("─" * 50)


async def parse_html(tab: zd.Tab) -> None:
    """Parse HTML content from a webpage."""
    tag = await tab.query_selector(".title")

    print("─ Scraped HTML ───────────────────────────────────")
    print(tag.text.strip())
    print("─" * 50)


async def start() -> None:
    """Start a browser, open a page, then keep the collector alive."""
    browser = await zd.start(
        browser_executable_path="/usr/bin/google-chrome-stable",
        user_data_dir=str(Path.home() / ".config" / "google-chrome-nodriver"),
    )

    tab = await browser.get("about:blank")

    await tab.send(cdp.network.enable())
    tab.add_handler(cdp.network.RequestWillBeSent, handler)

    tab = await browser.get("https://httpbin.org/")

    previous_url = None
    while True:
        if tab.url == previous_url:
            await asyncio.sleep(1)
            continue

        previous_url = tab.url

        if tab.url == "https://httpbin.org/":
            await parse_html(tab)


if __name__ == "__main__":
    asyncio.run(start())
