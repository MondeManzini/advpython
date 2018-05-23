from contextlib import contextmanager

@contextmanager
def test_context(context=''):
    # __enter__
    print 'entering',context, 'context'
    yield 'my context %s' % context
    # __exit__
    print 'closing', context

