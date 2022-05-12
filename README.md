# Get CyberArk data through API
I implemented a simple script to retrieve the root password list from a CyberArk account through **[CyberArk
REST API](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/WebServices/Implementing%20Privileged%20Account%20Security%20Web%20Services%20.htm?tocpath=Developer%7CREST%20APIs%7C_____0)**.

If you want to use it, you need to modify the _configs.py_ file:
- **USER**, your CyberArk username used to log on your vault
- **PASSWORD**, your CyberArk vault password
- **IP_LIST**, the ip list of remote machines
- **URI**, in my case, I have a radius authentication method, so I need to concatenate my password and an OTP from
a QR Code URI
- **API_URL**, you need to add your CyberArk domain vault to the current string

In general, you need to get a _session token_, create a _GET_ or _POST_ request based on the data you want to retrieve and close the opened session.
In my case:
1. `get_session_token( ... )` function creates a **[Logon RADIUS Authentication](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/SDK/CyberArk%20Authentication%20-%20Logon_v10.htm?tocpath=Developer%7CREST%20APIs%7CAuthentication%7CLogon%7C_____1)** request to get the session token
2. `get_account( ... )` function creates an **[Account](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/SDK/GetAccounts.htm?tocpath=Developer%7CREST%20APIs%7CAccounts%7C_____1)** request to get the account information with the IP I'm looking for
3. `get_password( ... )` function creates a **[Password](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/WebServices/GetPasswordValueV10.htm?tocpath=Developer%7CREST%20APIs%7CAccounts%7CAccount%20actions%7C_____5)** request based on the account id
4. `close_session ( ... )` function creates a **[Logoff RADIUS](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/WebServices/API-logoff-LP.htm?tocpath=Developer%7CREST%20APIs%7CAuthentication%7CLogoff%7C_____0)** request to close the opened session