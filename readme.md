# Copier Python project template

[Copier][copier-url] template to quickly setup a Python project shell.

Maintained primarily for personal use.


Setup using a Docker image with Copier:
```sh
docker run --rm -it -v ${pwd}/workflow:/usr/src/copier ghcr.io/ejoosterop/docker-copier copier copy https://github.com/EJOOSTEROP/copier-python.git /usr/src/copier
```

Summary of template:
- Python Project with src and tests folders.
- [pyproject.toml][toml-url] file for project metadata and tool configuration.
- Git installed and standard .gitignore file.
- VS Code devcontainer setup; includes VS Code extensions.
- Using [Poetry][poetry-url] for dependency management.
- [Ruff][ruff-url] and other linting tools.
- [Pre-commit][precommit-url] hooks for Git.
- [Nox][nox-url] to run tools in separate Python environment.
- MIT license, readme.md, empty changelog.md.
- Optional .dockerignore.

[copier-url]: https://github.com/copier-org/copier
[nox-url]: https://nox.thea.codes/en/stable/
[poetry-url]: https://python-poetry.org/
[precommit-url]: https://pre-commit.com/
[ruff-url]: https://beta.ruff.rs/docs/
[toml-url]: https://peps.python.org/pep-0621/
[toml-spec-url]: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
