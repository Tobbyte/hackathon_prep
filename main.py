"""Create Email from username."""

from fist_task import get_user_name
from second_task import remove_special_characters
from third_task import make_email_adresse


def main() -> None:
    """Orchestrate stuff."""
    user_name: str = get_user_name()
    user_name_clean: str = remove_special_characters(user_name)
    user_name_with_atexample: str = make_email_adresse(user_name_clean)
    print(user_name)
    print(user_name_clean)
    print(user_name_with_atexample)


if __name__ == "__main__":
    main()
