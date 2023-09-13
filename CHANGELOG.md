# Changelog
All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [Unreleased]

### Changed
- Question for PyPi URL in copier.yaml
- Update cli.py, test_001.py formatting so it better passes linting on first commit.
- GitHub bug report template now refers to package name (as opposed to Hydra)
- README.md updates: logo URL, project image URL, shields URL and smaller size.

### Removed
- Removed boilerplate code in __init__.py so it passes linting. Not certain the code was desired in the first place.

## [v0.6.1] 2023-09-13

### Added
- .gitignore for line endings. See [github](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings).

## [v0.6.0] 2023-09-12

### Added
- Shield repository file
- Copier will ask branch name for git init (defaults to main)
- GitHub template for bug report, feature request and pull request (using Facebook Reasearch' Hydra project's templates)
- CONTRIBUTING.md file (Also based on Hydra, but significantly simplified)

### Changed
- README.md scaffold.
- File name captalizations (LICENSE.txt, README.md)

### Removed
- Unused copier.yaml versions

## [v0.5.5] 2023-09-12

### Added
- Expand changelog.md template
- Add package version as a copier variable (default to 0.0.1)
- Add message to set python interpreter path for VS Code after copy is performed.
- Initiate Git with main branch when creating devcontainer
- Git user and email are set to that of the code author

### Fixed
- devcontainer post create commands

## [v0.5.0] 2023-09-12

### Added
- First mostly complete template

### Fixed
- None

### Changed
- None

### Removed
- None
