# Template documentation repository

This repository is a template allowing easy creation of python repository with a full documnentation automatisation.

## Usage

You can rename the `src` folder to whichever name you want for your source code (library name if it is a library)

Once done you need to replace `src` to your new name in the following files :

- `scripts/generate_index.py`
- `scripts/generate_references.py`
- `.github/workflows/generate_gh_pages.yml`
- `.github/workflows/tag_latest_release_gh_pages.yml`

## First set-up

Once you have set up everything you can do the following commands :

```bash
python -m venv venv
source venv/bin/activate
pip install -e .
mike deploy [version] latest
mike set-default latest
```

All those commands will build a first version `[version]` of your doc, tag it as the latest and use it by default. You
can then do the following command to check the built version locally :

```bash
mike serve
```

## Update the documentation

To check how your current doc would look like without adding it to the distant documentation you can use the following
command:

```bash
mkdocs serve
```

Once you are ok with the changes you can either push your changes to your `main` branch which will trigger an automatic
update of your doc.

Or you can use the following command

```bash
mike deploy [--push] [version]
```

- `--push` will allow to push the new version of your doc directly to the distant one.
- `version` is the version number of your doc, you can use an existing number to override an existing doc

## Change default version

If you want to change which version is displayed by default, you can use the following command :

```bash
mike alias [version] latest
```

With the previous settings you made that the default version used is the one with the alias `latest` this command allows
you to change which branch has that alias