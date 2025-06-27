import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Igor",
            "last_name": "Rodrigues",
            "cpf": "517.799.698-05",
            "email": "igorr2693@gmail.com",
            "birth_date": "2002-04-23"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Igor",
            "last_name": "Rodrigues",
            "cpf": "517.799.698-03",
            "email": "igorr2693@gmail.com",
            "birth_date": "2002-04-23"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Igor"
        assert response.json[0]["last_name"] == "Rodrigues"
        assert response.json[0]["cpf"] == "517.799.698-05"
        assert response.json[0]["email"] == "igorr2693@gmail.com"

        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "2002-04-23T00:00:00Z"

        response = client.get('/user/%s' % invalid_user["cpf"])
        assert response.status_code == 400
