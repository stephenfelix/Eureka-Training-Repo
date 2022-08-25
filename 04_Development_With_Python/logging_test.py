import logging

#logging.basicConfig(filename=logname, filemode='a')

foo_logger = logging.getLogger('foo')
foo_logger.setLevel(logging.INFO)
foo_logger.addHandler(logging.FileHandler("foo.log"))
foo_logger.error("Error from Foo")

foobar_logger = logging.getLogger('foo.bar')
foobar_logger.setLevel(logging.DEBUG)
foobar_logger.addHandler(logging.FileHandler("foo.bar.log"))
foobar_logger.error("Error from Foo.Bar")
