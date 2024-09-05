import pytest
import requests


class TestYandexDisk:

    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth y0_AgAAAAAoBlASAADLWwAAAAEQAZP1AADLZacQbUFOfqS1I80xy5ngIu8rqQ'
        }

    @pytest.mark.parametrize(
        'key, value, status',
        (
                ['path', 'Image', 201],
                ['path', 'Image', 409],
                ['pat', 'Image', 400],

        )
    )
    def test_create_folder(self, key, value, status):
        params = {
            key: value
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=self.headers)
        assert response.status_code == status
