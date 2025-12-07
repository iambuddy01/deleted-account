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

try:
    from X.helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, Numeric, String, UnicodeText


class Filters(BASE):
    __tablename__ = "filters"
    chat_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, chat_id, keyword, reply, f_mesg_id):
        self.chat_id = str(chat_id)
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id

    def __eq__(self, other):
        return bool(
            isinstance(other, Filters)
            and self.chat_id == other.chat_id
            and self.keyword == other.keyword
        )


Filters.__table__.create(checkfirst=True)


def get_filter(chat_id, keyword):
    try:
        return SESSION.query(Filters).get((str(chat_id), keyword))
    finally:
        SESSION.close()


def get_filters(chat_id):
    try:
        return SESSION.query(Filters).filter(Filters.chat_id == str(chat_id)).all()
    finally:
        SESSION.close()


def add_filter(chat_id, keyword, reply, f_mesg_id):
    to_check = get_filter(chat_id, keyword)
    if not to_check:
        adder = Filters(str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    else:
        rem = SESSION.query(Filters).get((str(chat_id), keyword))
        SESSION.delete(rem)
        SESSION.commit()
        adder = Filters(str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return False


def remove_filter(chat_id, keyword):
    to_check = get_filter(chat_id, keyword)
    if not to_check:
        return False
    else:
        SESSION.delete(to_check)
        SESSION.commit()
        return True
