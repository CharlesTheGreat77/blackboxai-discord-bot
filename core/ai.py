import requests
import json
import re
from typing import Optional, Tuple

def blackbox_ai(question: str) -> Optional[Tuple[str, str]]:
    '''
    function to send request to blackbox.ai api 
    returns sources and response
    '''
    session = requests.Session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1'})
    response = session.get('https://www.blackbox.ai')
    session_id = response.cookies.get('sessionId')

    data = {
        "messages": [
            {
                "id": f"1LmqRdE", # random id
                "content": f"{question}", # question to send to api
                "role": "user" # not sure if this could be changed??
            }
        ],
        "id": "1LmqRdE",
        "previewToken": None,
        "userId": "00bcbbca-fd66-46ee-98ab-87aa58fe1298",
        "codeModelMode": True,
        "agentMode": {},
        "trendingAgentMode": {},
        "isMicMode": False,
        "isChromeExt": False,
        "githubToken": None,
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "visitFromURL": None
    }
    content_length = len(json.dumps(data))

    headers = {
        'Host': 'www.blackbox.ai',
        'Content-Length': f'{str(content_length)}',
        'Sec-Ch-Ua': '"Not A Brand";v="124", "Chromium";v="124", "Google Chrome"',
        'Sec-Ch-Ua-Platform': '"macOS"', # change platform & user agent as necessary
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://www.blackbox.ai',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.blackbox.ai/',
        'Accept-Encoding': 'identity',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    cookies = {
        'sessionId': f'{session_id}',
        'intercom-id-jlmqxicb': '435ebd45-eff0-4e09-9d7a-ea60f09a5072',
        'intercom-session-jlmqxicb': '',
        'intercom-device-id-jlmqxicb': '4b7495aa-20c0-4c64-95d2-cc4b88ab26cf'
    }

    response = requests.post('https://www.blackbox.ai/api/chat', headers=headers, cookies=cookies, json=data)

    match = re.search(r"Sources:(.*?)\n\n(.*)", response.text, re.DOTALL)
    if match:
        sources = match.group(1).strip()
        response = match.group(2).strip()
        return sources, response