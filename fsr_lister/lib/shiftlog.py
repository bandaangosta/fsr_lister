import requests
from fsr_lister import app

REQUEST_STATUS_CODE_OK = 200


def getData():
    token = app.config["TOKEN"]
    api_call_url = app.config["API_CALL_URL"]
    auth_token_string = "Basic " + token
    api_headers = {
        "Authorization": auth_token_string,
    }

    params = {
        "maxEntries": "100",
        "cmdlEntry": "true",
    }
    result = requests.get(api_call_url, headers=api_headers, params=params)
    output_data = []
    if result.status_code == REQUEST_STATUS_CODE_OK:
        data = result.json()
        if data:
            for entry in data:
                if "full" in entry["subject"].lower():
                    output_data.append(
                        {
                            "entryType": entry["entryType"],
                            "subject": entry["subject"],
                            "start": entry["start"],
                            "end": entry["end"],
                            "location": entry["location"],
                        }
                    )
    return output_data
