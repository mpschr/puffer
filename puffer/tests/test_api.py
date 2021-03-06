import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from puffer.api import API

def test_api_get_request():
  '''
    Test simply api get request
  '''

  with patch('puffer.api.OAuth2Session') as mocked_oauth2:
    mocked_session = MagicMock()

    mocked_response = MagicMock()
    mocked_response.content = bytes(json.dumps({'status': 'ok'}), encoding="utf-8")
    mocked_session.get.return_value = mocked_response

    mocked_oauth2.return_value = mocked_session

    api = API(client_id='1', client_secret='2', access_token='access_token')
    api.get(url="hey")

    mocked_session.get.assert_called_once_with(url='https://api.bufferapp.com/1/hey')

@raises(ValueError)
def test_api_get_request_no_access_token():
  '''
    Test simply api get request without access_token
  '''

  with patch('puffer.api.OAuth2Session') as mocked_oauth2:
    mocked_session = MagicMock()
    mocked_session.access_token = None

    mocked_oauth2.return_value = mocked_session

    api = API(client_id='1', client_secret='2')
    api.get(url="hey")

def test_api_post_request():
  '''
    Test simply api post request
  '''

  with patch('puffer.api.OAuth2Session') as mocked_oauth2:
    mocked_session = MagicMock()

    mocked_response = MagicMock()
    mocked_response.content = bytes(json.dumps({'status': 'ok'}), encoding="utf-8")
    mocked_session.post.return_value = mocked_response

    mocked_oauth2.return_value = mocked_session

    api = API(client_id='1', client_secret='2', access_token='access_token')
    api.post(url='hey', data='new=True')

    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    mocked_session.post.assert_called_once_with(
        url='https://api.bufferapp.com/1/hey', headers=headers, data='new=True')

@raises(ValueError)
def test_api_post_request_no_access_token():
  '''
    Test simply api post request without access_token
  '''

  with patch('puffer.api.OAuth2Session') as mocked_oauth2:
    mocked_session = MagicMock()

    mocked_session.access_token = None

    mocked_oauth2.return_value = mocked_session

    api = API(client_id='1', client_secret='2', access_token='access_token')
    api.post(url='hey', data='new=True')

def test_api_info():
  '''
    Test simple configuration retrieving
  '''

  with patch('puffer.api.OAuth2Session') as mocked_oauth2:
    mocked_session = MagicMock()

    mocked_response = MagicMock()
    mocked_response.content = bytes(json.dumps({'status': 'ok'}), encoding="utf-8")
    mocked_session.get.return_value = mocked_response

    mocked_oauth2.return_value = mocked_session

    api = API(client_id='1', client_secret='2', access_token='access_token')
    info = api.info

    url = 'https://api.bufferapp.com/1/info/configuration.json'
    mocked_session.get.assert_called_once_with(url=url)
    eq_(info.status, 'ok')
