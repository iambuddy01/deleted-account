#MIT License

#Copyright (c) 2024 deleted-account

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import aiohttp
from yourls import YOURLSClient
from yourls.exceptions import YOURLSKeywordExistsError, YOURLSURLExistsError

YOURLS_URL = None
YOURLS_KEY = None


async def shorten_url(url, keyword):
    if not YOURLS_URL or not YOURLS_KEY:
        return "API ERROR"

    url_checked = await url_check(url)
    if url_checked:
        yourls = YOURLSClient(YOURLS_URL, signature=YOURLS_KEY)
        try:
            shorturl = yourls.shorten(url, keyword).shorturl
            result = shorturl
        except (YOURLSURLExistsError, YOURLSKeywordExistsError):
            result = "KEYWORD/URL Exists"
    else:
        result = "INVALID URL"
    return result


async def url_check(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return resp.status == 200
    except aiohttp.ClientError:
        return False
