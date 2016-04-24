'''
Created on Apr 23, 2016

@author: ivan
'''
import unittest
from server import db, app
import threading
import model
from flask import appcontext_pushed


def debug(*args, **kwargs):
    print('CONTEXT PUSHED',args,kwargs)
  
appcontext_pushed.connect(debug,app)  


class Test(unittest.TestCase):


    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ebooks:ebooks@localhost/ebooks' 
        self.ctx=app.test_request_context()
        self.ctx.push()


    def tearDown(self):
        self.ctx.pop()


    def test_db(self):
        n=model.Format.query.filter().count()
        self.assertEqual(n, 17)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_db']
    unittest.main()