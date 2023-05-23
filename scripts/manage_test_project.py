import argparse
import shutil
from pathlib import Path

from django.core.management import call_command

TEST_PROJECT_NAME: str = "test_project"

BASE_DIR: Path = Path(__file__).parent.parent
PATH_TO_TEMPLATE: Path = BASE_DIR / "project_template"
PATH_TO_TEST_PROJECT: Path = BASE_DIR / TEST_PROJECT_NAME


def main() -> None:
    parser = argparse.ArgumentParser(description="Set up and tear down test projects.")
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove test project directory.",
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create test project.",
    )
    args = parser.parse_args()
    if args.clean:
        # Recursively remove dir for test project if it already exists
        try:
            shutil.rmtree(PATH_TO_TEST_PROJECT)
        except FileNotFoundError:
            pass
    if args.create:
        # Create dir for test project
        PATH_TO_TEST_PROJECT.mkdir(exist_ok=True)
        # Call django-admin command
        call_command(
            "startproject",
            TEST_PROJECT_NAME,
            str(PATH_TO_TEST_PROJECT),
            extension=["md", "py", "toml"],
            template=str(PATH_TO_TEMPLATE),
        )


if __name__ == "__main__":
    main()
