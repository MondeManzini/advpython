class test_context(object):
    def __enter__(self):
        print 'entering context'
	return 'my context'
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'closing'

