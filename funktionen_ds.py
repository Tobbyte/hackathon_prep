def display_email_address(email: str) -> str:
    """Zeigt die E-Mail-Adresse an und gibt sie zurueck."""
    print(email)
    return email


def test_display_email_address(capsys) -> None:
    """Testet Ausgabe und Rueckgabewert."""
    result = display_email_address("user123@example.com")
    captured = capsys.readouterr()
    assert result == "user123@example.com"
    assert captured.out == "user123@example.com\n"
