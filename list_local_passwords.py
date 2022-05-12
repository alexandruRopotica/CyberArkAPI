from utils import *


if __name__ == '__main__':
    radius_password = generate_password(configs.URI, configs.PASSWORD)
    session_token = get_session_token(radius_password)
    for ip in configs.IP_LIST:
        account = get_account(session_token, ip)
        account_id = account['value'][0]['id']
        local_password = get_password(session_token, account_id)
        print(f'IP: {ip} \t Local password: {local_password}')
    close_session(session_token)
