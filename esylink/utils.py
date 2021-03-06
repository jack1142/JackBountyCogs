import json
from typing import Any, Dict, Union

import aiohttp


async def json_or_text(resp: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    """
    Returns json dict, if response's content type is json,
    or raw text otherwise.

    Parameters
    ----------
    resp: `aiohttp.ClientResponse`
        Response object

    Returns
    -------
    `dict` or `str`
        Response data.
    """
    text = await resp.text(encoding="utf-8")
    content_type = resp.headers.get(aiohttp.hdrs.CONTENT_TYPE, "")
    # this API seems to be responding with a bit untypical content type header
    if content_type in ("application/javascript", "application/json"):
        data = json.loads(text)
        assert isinstance(data, dict), "mypy"
        return data
    return text
