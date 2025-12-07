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

import re


class IntervalHelper:
    class IntervalError(Exception):
        pass

    interval_re = re.compile(r"^(\d+)(w|d|h|m)?$")

    def __init__(self, _interval):
        self._interval = _interval
        if not self.interval_ok():
            raise Exception("Invalid interval format.")

    def interval_ok(self):
        if IntervalHelper.interval_re.match(self._interval):
            return True
        return False

    def to_secs(self):
        m = IntervalHelper.interval_re.match(self._interval)
        num, unit = m.groups()
        num = int(num)

        if not unit:
            unit = "m"

        if unit == "m":
            return [num * 60, num, "minute" if num == 1 else "minutes"]
        elif unit == "h":
            return [num * 60 * 60, num, "hour" if num == 1 else "hours"]
        elif unit == "d":
            return [num * 60 * 60 * 24, num, "day" if num == 1 else "days"]
        elif unit == "w":
            return [num * 60 * 60 * 24 * 7, num, "week" if num == 1 else "weeks"]

    interval = property(lambda self: self._interval)
