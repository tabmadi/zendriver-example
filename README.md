# 🐍 Python Project Template
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

A modern Python repository template that provides a solid foundation for your next Python project. This template follows the `src` layout for better package management and includes essential tools for development, testing, and CI/CD.

## ✨ Features

- 🐍 **Python Focused**: Optimized for modern Python development (3.12+)
- 📁 **Src Layout**: Follows [Python's recommended `src` layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- 📦 **Modern Dependency Management**: Powered by `uv` for lightning-fast package management
- 🛠️ **Linting & Formatting**: Pre-configured with `ruff`
- 🔧 **Modern Tooling**: Pre-configured development workflow tools including Lefthook, Mise, Cocogitto, and Act
- 🏥 **Community Health Files**: Includes standard files for project governance
- 🤝 **GitHub Integration**: Pre-configured issue and pull request templates

## 🚀 Quick Start

### Prerequisites

- [Mise](https://mise.jdx.dev/) - Tool version manager
- [Docker](https://www.docker.com/) - Required for running GitHub Actions locally with Act

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheRealZurvan/python-project-template.git
   cd python-project-template
   ```

2. **Setup environment**:
   ```bash
   # Install mise (if not already installed)
   curl https://mise.run | sh
   
   # Install configured tools (python, uv, ruff, lefthook, cocogitto, act)
   mise install
   
   # Set up Python virtual environment and dependencies
   uv venv
   uv sync
   
   # Set up Git hooks
   lefthook install
   ```

## 🏃‍♂️ Usage

### Local CI Testing (Act)

If you have Docker installed, you can run GitHub Actions locally using `act`. This template includes a pre-configured mise task for testing pull request workflows:

```bash
mise run act-pr
```

This command uses `.github/act/pull_request.json` to simulate a pull request event.

## 🛠️ Development

### 🔧 Development Tools

- **Python**: The core programming language (version specified in `.tool-versions`).
- **UV**: An extremely fast Python package and project manager, replacing `pip`, `pip-tools`, and `poetry`.
- **Ruff**: An extremely fast Python linter and code formatter, written in Rust.
- **Mise**: Ensures consistent tool versions (python, uv, ruff, cocogitto, lefthook, act) across different environments.
- **Lefthook**: Git hooks manager that runs checks (like `ruff`) before commits and pushes.
- **Cocogitto**: Enforces Conventional Commits and automates changelog generation.
- **Act**: Runs GitHub Actions locally for faster feedback loops.

### 🪝 Git Hooks & Conventional Commits

This project uses **Lefthook** for Git hooks and follows **Conventional Commits**.
- **Commit-msg**: Validates commit messages using `cog verify`.
- **Pre-push**: Runs checks before pushing to the remote repository.

## 📁 Project Structure

This project follows the [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/    # Structured issue templates
│   └── act/               # Local CI testing configuration
├── scripts/               # Helper scripts
├── src/                   # Source code
│   └── main.py            # Main entry point
├── tests/                 # Test suite (if applicable)
├── .lefthook.yml          # Git hooks configuration
├── .tool-versions         # Mise tool versions
├── LICENSE                # Apache License 2.0
├── pyproject.toml         # Python project configuration and dependencies
├── README.md              # You are here! 📍
├── SECURITY.md            # Security policy
└── mise.toml              # Mise tasks configuration
```

## ✏️ Customization Guide

### README.md
- Replace this content with information about your project.
- Include sections such as Project description, Usage examples, and API documentation.

### LICENSE
- The template includes the Apache License 2.0.
- Update the copyright notice or replace the file with your preferred license.

### Community Files
- **CODE_OF_CONDUCT.md**: Update the contact information in the "Enforcement" section.
- **SECURITY.md**: Update contact details and supported versions policy.

### Templates
- **Issue Templates**: Modify fields, labels, and descriptions in `.github/ISSUE_TEMPLATE/`.
- **Pull Request Template**: Adjust the checklist items in `.github/PULL_REQUEST_TEMPLATE.md`.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔒 Security

Please see [SECURITY.md](SECURITY.md) for our security policy.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

**Happy coding! 🎉** If you find this template useful, please give it a ⭐️
