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

import threading

from sqlalchemy import Column, String

from X.helpers.SQL import BASE, SESSION

# class set_req
# class get_req


class WhitelistUsers(BASE):
    __tablename__ = "pmapprove"
    user_id = Column(String(14), primary_key=True)
    username = Column(String(15))

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


class ReqUsers(BASE):
    __tablename__ = "getpmapprove"
    user_id = Column(String(14), primary_key=True)
    username = Column(String(15))

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


ReqUsers.__table__.create(checkfirst=True)

WhitelistUsers.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def set_whitelist(user_id, username):
    with INSERTION_LOCK:
        user = SESSION.query(WhitelistUsers).get(str(user_id))
        if not user:
            user = WhitelistUsers(str(user_id), str(username))
        else:
            user.username = str(username)

        SESSION.add(user)
        SESSION.commit()


def del_whitelist(user_id):

    with INSERTION_LOCK:
        user = SESSION.query(WhitelistUsers).get(str(user_id))
        if user:
            SESSION.delete(user)
            SESSION.commit()
        else:
            SESSION.close()
            return False


def get_whitelist(user_id):
    user = SESSION.query(WhitelistUsers).get(str(user_id))
    rep = ""
    if user:
        rep = str(user.username)

    SESSION.close()
    return rep


def set_req(user_id, username):
    with INSERTION_LOCK:
        user = SESSION.query(ReqUsers).get(str(user_id))
        if not user:
            user = ReqUsers(str(user_id), str(username))
        else:
            user.username = str(username)

        SESSION.add(user)
        SESSION.commit()


def get_req(user_id):
    user = SESSION.query(ReqUsers).get(str(user_id))
    rep = ""
    if user:
        rep = str(user.username)

    SESSION.close()
    return rep
