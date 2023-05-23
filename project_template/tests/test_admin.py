from django.test import Client


def test_admin_home_smoke_test(client: Client) -> None:
    response = client.get("/admin/")
    assert response.status_code == 302
