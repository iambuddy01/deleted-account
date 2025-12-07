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

from sqlalchemy import Column, Numeric, String, UnicodeText

from X.helpers.SQL import BASE, SESSION


class Note(BASE):
    __tablename__ = "note"
    user_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    f_mesg_id = Column(Numeric)

    def __init__(self, user_id, keyword, f_mesg_id):
        self.user_id = str(user_id)
        self.keyword = keyword
        self.f_mesg_id = int(f_mesg_id)


Note.__table__.create(checkfirst=True)


def get_note(user_id, keyword):
    try:
        return SESSION.query(Note).get((str(user_id), keyword))
    finally:
        SESSION.close()


def get_notes(user_id):
    try:
        return SESSION.query(Note).filter(Note.user_id == str(user_id)).all()
    finally:
        SESSION.close()


def add_note(user_id, keyword, f_mesg_id):
    to_check = get_note(user_id, keyword)
    if not to_check:
        adder = Note(str(user_id), keyword, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Note).get((str(user_id), keyword))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Note(str(user_id), keyword, f_mesg_id)
    SESSION.add(adder)
    SESSION.commit()
    return False


def rm_note(user_id, keyword):
    to_check = get_note(user_id, keyword)
    if not to_check:
        return False
    rem = SESSION.query(Note).get((str(user_id), keyword))
    SESSION.delete(rem)
    SESSION.commit()
    return True
