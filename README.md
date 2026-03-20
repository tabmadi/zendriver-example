# 🕷️ Zendriver Passive Scraping Example
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

An example project demonstrating how to do passive web scraping with [Zendriver](https://github.com/stephanlensky/zendriver) using the Chrome DevTools Protocol (CDP). Instead of actively fetching pages, this approach listens to network events as they happen in a real browser session — intercepting XHR/JSON responses and parsing HTML without triggering additional requests.

## ✨ Features

- 🕵️ **Passive Scraping**: Intercepts network traffic passively via CDP events rather than driving requests
- 🌐 **XHR Interception**: Captures JSON API responses using `Network.requestWillBeSent` hooks
- 📄 **HTML Parsing**: Queries live page DOM via CSS selectors
- 🔁 **URL Change Detection**: Monitors tab navigation to trigger page-specific logic
- 📦 **Modern Dependency Management**: Powered by `uv` for lightning-fast package management
- 🛠️ **Linting & Formatting**: Pre-configured with `ruff`

## 🚀 Quick Start

### Prerequisites

- Python 3.14+
- [Mise](https://mise.jdx.dev/) - Tool version manager
- Google Chrome installed at `/usr/bin/google-chrome-stable`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheRealZurvan/zendriver-example.git
   cd zendriver-example
   ```

2. **Setup environment**:
   ```bash
   # Install mise (if not already installed)
   curl https://mise.run | sh

   # Install configured tools (python, uv, ruff)
   mise install

   # Set up Python virtual environment and dependencies
   uv venv
   uv sync
   ```

## 🏃‍♂️ Usage

Run the scraper with:

```bash
uv run src/main.py
```

The script opens `https://httpbin.org/` in a Chrome instance and demonstrates:
- Intercepting outbound requests that expect a JSON response and printing the response body
- Parsing an HTML element from the page using a CSS selector

## 🛠️ Development

### 🔧 Development Tools

- **Python**: The core programming language (version specified in `.tool-versions`).
- **UV**: An extremely fast Python package and project manager, replacing `pip`, `pip-tools`, and `poetry`.
- **Ruff**: An extremely fast Python linter and code formatter, written in Rust.
- **Mise**: Ensures consistent tool versions (python, uv, ruff) across different environments.

### 🪝 Git Hooks & Conventional Commits

This project uses **Lefthook** for Git hooks and follows **Conventional Commits**.
- **Commit-msg**: Validates commit messages using `cog verify`.
- **Pre-push**: Runs checks before pushing to the remote repository.

## 📁 Project Structure

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/    # Structured issue templates
│   └── act/               # Local CI testing configuration
├── scripts/               # Helper scripts
├── src/                   # Source code
│   └── main.py            # Scraper entry point
├── .lefthook.yml          # Git hooks configuration
├── .tool-versions         # Mise tool versions
├── LICENSE                # Apache License 2.0
├── pyproject.toml         # Python project configuration and dependencies
├── README.md              # You are here! 📍
├── SECURITY.md            # Security policy
└── mise.toml              # Mise tasks configuration
```

## 💡 How It Works

The scraper registers a CDP event handler on `Network.requestWillBeSent`. For every outgoing request with `Accept: application/json`, it waits briefly and then fetches the response body via `Network.getResponseBody`. HTML content is scraped by querying CSS selectors on the live tab DOM.

A passive loop monitors `tab.url` for changes, triggering page-specific parsing logic whenever navigation occurs — allowing the browser to be used normally while scraping runs in the background.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

**Happy scraping! 🎉**
