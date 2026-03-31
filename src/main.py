"""Minimal data collector."""

import asyncio
from pathlib import Path

import zendriver as zd
from cachetools import TTLCache
from zendriver import cdp

pending_request_ids = TTLCache(maxsize=1024, ttl=30)


async def on_request(event: cdp.network.RequestWillBeSent, _tab: zd.Tab) -> None:
    """Track JSON XHR requests by request ID."""
    headers = event.request.headers

    if headers.get("accept") != "application/json":
        return

    pending_request_ids[event.request_id] = True


async def on_loading_finished(event: cdp.network.LoadingFinished, tab: zd.Tab) -> None:
    """Fetch response body once fully loaded."""
    if event.request_id not in pending_request_ids:
        return

    pending_request_ids.pop(event.request_id, None)

    body, _ = await tab.send(cdp.network.get_response_body(request_id=event.request_id))

    print("─ Scraped XHR request ────────────────────────────")
    print(body)
    print("─" * 50)


async def parse_html(tab: zd.Tab) -> None:
    """Parse HTML content from a webpage."""
    tag = await tab.select(".title", timeout=10)

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
    tab.add_handler(cdp.network.RequestWillBeSent, on_request)
    tab.add_handler(cdp.network.LoadingFinished, on_loading_finished)

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
