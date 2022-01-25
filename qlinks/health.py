import logging

import requests

logger = logging.getLogger(__name__)


def check_url(url):
    try:
        return 200 <= requests.get(url).status_code < 400
    except requests.RequestException:
        logger.exception('Failed to fetch: %s', url)
        return False
