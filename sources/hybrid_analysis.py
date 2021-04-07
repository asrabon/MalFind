import requests


SEARCH_URL = "https://hybrid-analysis.com/api/v2/search/hash"
SAMPLE_URL = "https://hybrid-analysis.com/sample/{}/{}"
SAMPLE_NO_JOB_ID_URL = "https://hybrid-analysis.com/sample/{}"


def search(file_hash, api_key):
    r = requests.post(
        SEARCH_URL,
        headers={
            'User-Agent': 'Falcon Sandbox',
            "api-key": api_key
        },
        data = {
            "hash": file_hash
        },
        timeout=30
    )
    search_submissions = r.json()
    
    if len(search_submissions) > 0:
        sample_urls = []
        for entry in search_submissions:
            sha256, job_id = entry["sha256"], entry["job_id"]

            if job_id:
                sample_urls.append(SAMPLE_URL.format(entry["sha256"], entry["job_id"]))
            else:
                sample_urls.append(SAMPLE_NO_JOB_ID_URL.format(entry["sha256"]))
        return sample_urls
    return None
