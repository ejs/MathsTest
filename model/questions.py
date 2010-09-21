import shelve
from lib.quizz_master import Quizz


class QuestionStore(object):
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.db = shelve.open(dbfile)

    def store_quizz(self, quizz):
        self.db[quizz.quizzid] = quizz
        self.db.sync()

    def load_quizz(self, quizzid):
        if quizzid not in self.db:
            self.db[quizzid] = Quizz(quizzid)
            self.db.sync()
        return self.db[quizzid]

    def latest_timestamp(self):
        return max(self.db)
