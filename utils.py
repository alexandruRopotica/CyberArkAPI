import pyotp
import configs
from CARequest import CARequest


def generate_password(uri: str, password: str):
    totp = pyotp.parse_uri(uri)
    otp = totp.now()
    radius_password = password + otp
    return radius_password


def get_session_token(radius_password: str):
    logon_request = CARequest(
        url=configs.API_URL + 'auth/RADIUS/Logon',
        headers={"content-type": "application/json"},
        data={"username": f"{configs.USER}", "password": f"{radius_password}", "concurrentSession": True},
        method='POST')
    logon_request.request()
    return logon_request.get_content()


def get_account(session_token: str, ip_to_search: str):
    account_request = CARequest(
        url=configs.API_URL + 'Accounts?search=' + ip_to_search,
        headers={"Authorization": session_token, "content-type": "application/json"},
        data={},
        method='GET'
    )
    account_request.request()
    return account_request.get_content()


def get_password(session_token: str, account_id: str):
    password_request = CARequest(
        url=configs.API_URL + 'Accounts/' + account_id + '/Password/Retrieve',
        headers={"Authorization": session_token, "content-type": "application/json"},
        data={},
        method='POST'
    )
    password_request.request()
    return password_request.get_content()


def close_session(token: str):
    logoff_request = CARequest(
        url=configs.API_URL + 'Auth/Logoff',
        headers={"Authorization": token, "content-type": "application/json"},
        data={},
        method='POST'
    )
    logoff_request.request()
    if logoff_request.get_status_code() == 200:
        print('Logoff succeeded')
    else:
        print('Logoff failed')
