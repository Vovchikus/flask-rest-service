Example of REST service using Flask framework and Mongoengine

Installation (you should have python 2.7, pip and virtualenv already installed):

1. [sudo] pip install flask (http://flask.pocoo.org/)
2. [sudo] pip install flask-restful (http://flask-restful-cn.readthedocs.org/en/0.3.4/installation.html) (compomemt to build restful api)
3. [sudo] pip install flask-wtf (forms)
4. [sudo] pip install flask-mongoengine (orm to work with queries) 

Order Example:
Simple example of Document "Order" which has simple fields and nested field Item (e.g. {order: {article: ...}})
