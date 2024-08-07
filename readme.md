# Copier Python project template

[Copier][copier-url] template to quickly setup a Python project shell.

Suggestions are welcome. Template is maintained primarily for personal use.

Setup can be done with a standard `copier copy https://github.com/EJOOSTEROP/copier-python.git .` command.

Alternatively use a Docker image with Copier if Copier is not installed on your system (this creates a `workflow` folder locally):
```sh
docker run --rm -it -v ${pwd}/workflow:/usr/src/copier ghcr.io/ejoosterop/docker-copier copier copy gh:EJOOSTEROP/copier-python.git /usr/src/copier
```

## Summary
- Python Project with src and tests folders.
- [pyproject.toml][toml-url] file for project metadata and tool configuration.
- Git installed and standard .gitignore file.
- VS Code devcontainer setup; includes VS Code extensions.
- Using [Poetry][poetry-url] for dependency management.
- For linting and formatting: [Ruff][ruff-url], [Black][black-url] and other (from VS Code extensions).
- [Pre-commit][precommit-url] hooks for Git.
- [Nox][nox-url] to run tools in separate Python environment.
- MIT license, readme.md, empty changelog.md.
- Pytest, MyPy, [toml-sort][toml-sort-url] installed.
- Optional .dockerignore.
- Setup to use Github as a repository. Does not account for alternative.

## Development note
Somehow copier takes the template from the latest released version on GitHub instead of the local version.

## Roadmap
- [x] Create useable readme.md shell.
- [ ] Github actions. Some examples:
    - https://github.com/pappasam/toml-sort/tree/main/.github/workflows
    - https://github/workflows/publish-to-test-pypi.yml
- [x] Github templates for issues, feature requests.
- [ ] Setup documentation. Example https://github.com/pappasam/toml-sort/blob/main/readthedocs.yaml.

[black-url]: https://black.readthedocs.io/en/stable/
[copier-url]: https://github.com/copier-org/copier
[nox-url]: https://nox.thea.codes/en/stable/
[poetry-url]: https://python-poetry.org/
[precommit-url]: https://pre-commit.com/
[ruff-url]: https://beta.ruff.rs/docs/
[toml-url]: https://peps.python.org/pep-0621/
[toml-spec-url]: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
[toml-sort-url]: https://toml-sort.readthedocs.io/en/latest/
