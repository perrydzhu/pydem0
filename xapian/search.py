# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xapian

kw = ["苹果", "成都"]

db = xapian.WritableDatabase("db/test", xapian.DB_OPEN)
parser = xapian.QueryParser()




# for w in kw:
#     print w
#     query = parser.parse_query(w)
#     query_list.append(query)

query = parser.parse_query(kw)
enquire = xapian.Enquire(db)
enquire.set_query(query)
for m in enquire.get_mset(0, 30):
    print m.docid


