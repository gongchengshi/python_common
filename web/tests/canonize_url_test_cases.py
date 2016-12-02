# -*- coding: utf-8 -*-

#No current support for Internationalized Domain Names or domain name internationalization.
class TestCases:
    canonical_urls = [
        'http://www.example.com/',
        'http://example.com:8080/',
        'http://www.example.com/foo/bar.html',
        'http://example/',
        'http://example.com/~jane',
        'http://example.com/one/two',
        'http://example.com/one/two/',
        'http://example.com/?a=7&b=9',
        'http://example.com/one/two?a=7&b=9',
        'http://example.com/one/two/?a=7&b=9',
        'http://www.example.com/foo/bar.html?a=7&b=9',
        'http://www.example.com/foo/bar.html/?a=7&b=9',
        'http://example/?a=7&b=9',
        'http://example/one/two?a=7&b=9',
        'http://example/one/two/?a=7&b=9',
        'http://example.com/?q=%E2%85%A0',
    ]

    #scheme = alpha *(alpha | digit | "+" | "-" | ".")
    invalid_urls = [
        'dummy',
        'http://',
        'http:///',
        'http://',
        'com$://example.com/',
        '3com://example.com/',
        # 'http://.com/',
        # 'file:c:\\dir1\\file.txt',
        # 'http://ex$ample/'
    ]

    case_sensitivity = {
        'HTTP://www.example.com': 'http://www.example.com/',
        'HTTP://www.SUB.example.COM': 'http://www.sub.example.com/',
    }

    slashes = {
        'http://example': 'http://example/',
        'http://www.example.com': 'http://www.example.com/',
        'http://www.example.com/': 'http://www.example.com/',
        'http://www.example.com:8080': 'http://www.example.com:8080/',
        'http://www.example.com/one': 'http://www.example.com/one',
        'http://www.example.com:8080/one': 'http://www.example.com:8080/one',
        'http://www.example.com/one/': 'http://www.example.com/one/',
        'http://www.example.com/one?a=1': 'http://www.example.com/one?a=1',
        'http://www.example.com/one/?a=1': 'http://www.example.com/one/?a=1',
        'http://www.example.com/foo//': 'http://www.example.com/foo/',
        'http://www.example.com//foo//': 'http://www.example.com/foo/',
        'http://www.example.com/foo///bar//': 'http://www.example.com/foo/bar/',
    }

    scheme = {
        'irc://domain.test/room': 'irc://domain.test/room',
        'http://www.example.com:443': 'http://www.example.com:443/',
        'ftp://www.example.com': 'ftp://www.example.com/',
    }

    add_scheme = {
        'www.example.com': 'http://www.example.com/',
        'www.example.com/one/': 'http://www.example.com/one/',
        'www.example.com:80': 'http://www.example.com/',
        'www.example.com:21': 'ftp://www.example.com/',
        'www.example.com:443': 'https://www.example.com/',
        'example.com:80': 'http://example.com/',
        'example.com:21': 'ftp://example.com/',
        'example.com:443': 'https://example.com/',
        'example.com:443/': 'https://example.com/',
        'example.com:443/one': 'https://example.com/one',
        'example.com:9999': 'http://example.com:9999/',
        '127.0.0.1': 'http://127.0.0.1/',
    }

    fix_scheme = {
        #'htp://www.example.com': 'http://www.example.com/',
        #'htps://www.example.com': 'https://www.example.com/',
        'http//www.example.com': 'http://www.example.com/',
        'http//www.example.com:80': 'http://www.example.com/',
        'https//www.example.com': 'https://www.example.com/',
        'feed:http://domain/feed': 'http://domain/feed',
    }

    port = {
        'http://www.example.com:80': 'http://www.example.com/',
        'http://www.example.com:8080': 'http://www.example.com:8080/',
        'https://www.example.com:443': 'https://www.example.com/',
        'ftp://www.example.com:21': 'ftp://www.example.com/',
        'http://127.0.0.1:80': 'http://127.0.0.1/',
        'http://127.0.0.1:8080': 'http://127.0.0.1:8080/',
        'http://www.foo.com:80/foo': 'http://www.foo.com/foo',
        'http://www.foo.com:8000/foo': 'http://www.foo.com:8000/foo',
    }

    quoted_chars = {
        'http://example.com/%7Ejane': 'http://example.com/~jane',
        'http://example.com/%7ejane': 'http://example.com/~jane',
        'http://example.com/?q=1%2f2': 'http://example.com/?q=1%2F2',
        'http://www.example.com/one/two three/four': 'http://www.example.com/one/two%20three/four',
        'http://example.com/a/ä.txt': 'http://example.com/a/%E4.txt',
        'http://example.com/?q=Ç': 'http://example.com/?q=C%CC%A7',
        # replace '+' with '%20' in query string
        'http://example/one/two/?a=7+6&b=9': 'http://example/one/two/?a=7%206&b=9',
    }

    relative_paths = {
        'http://example.com/a/./b': 'http://example.com/a/b',
        'http://example.com/a/../a/b': 'http://example.com/a/b',
        'http://www.example.com/./': 'http://www.example.com/',
        'http://www.example.com/one/./two': 'http://www.example.com/one/two',
        'http://www.example.com/one/../two': 'http://www.example.com/two',
        'http://www.example.com/one/../../two': 'http://www.example.com/two',
        'http://www.example.com/one/../../two/../': 'http://www.example.com/',
        'http://www.example.com/one/two/../../two/../': 'http://www.example.com/',
        'http://www.example.com/one/two../': 'http://www.example.com/one/two../',
        'http://www.example.com/foo/bar/.': 'http://www.example.com/foo/bar/',
        'http://www.example.com/foo/bar/./': 'http://www.example.com/foo/bar/',
        'http://www.example.com/foo/.': 'http://www.example.com/foo/',
        'http://www.example.com/foo/./': 'http://www.example.com/foo/',
        'http://www.example.com/foo/bar/..': 'http://www.example.com/foo/',
        'http://www.example.com/foo/bar/../': 'http://www.example.com/foo/',
        'http://www.example.com/foo/bar/../baz': 'http://www.example.com/foo/baz',
        'http://www.example.com/foo/bar/../..': 'http://www.example.com/',
        'http://www.example.com/foo/bar/../../': 'http://www.example.com/',
        'http://www.example.com/foo/bar/../../baz': 'http://www.example.com/baz',
        'http://www.example.com/foo/bar/../../../baz': 'http://www.example.com/baz',
        'http://www.example.com/foo/bar/../../../../baz': 'http://www.example.com/baz',
        'http://www.example.com/./foo': 'http://www.example.com/foo',
        'http://www.example.com/../foo': 'http://www.example.com/foo',
        'http://www.example.com/foo.': 'http://www.example.com/foo',
        'http://www.example.com/.foo': 'http://www.example.com/.foo',
        'http://www.example.com/foo..': 'http://www.example.com/foo',
        'http://www.example.com/..foo': 'http://www.example.com/..foo',
        'http://www.example.com/./../foo': 'http://www.example.com/foo',
        'http://www.example.com/./foo/.': 'http://www.example.com/foo/',
        'http://www.example.com/foo/./bar': 'http://www.example.com/foo/bar',
        'http://www.example.com/foo/../bar': 'http://www.example.com/bar',
    }

    back_slashes = {
        'http://example.com\\test.html': 'http://example.com/test.html',
        'http://example.com\\a\\test.html': 'http://example.com/a/test.html',
        'http://example.com/a\\test.html': 'http://example.com/a%5Ctest.html',
    }

    query = {
        'http://www.example.com/one?': 'http://www.example.com/one',
        'http://www.example.com/one/?': 'http://www.example.com/one/',
        'http://example.com/?b=1&a=2': 'http://example.com/?a=2&b=1',
        'http://example.com/??b=1&a=2': 'http://example.com/?a=2&b=1',
        'http://example.com/?a=1&a=1': 'http://example.com/?a=1',
        'http://example.com/?a=1&a=': 'http://example.com/?a=&a=1',
        'http://example.com/?a=1&a': 'http://example.com/?a&a=1',
        'http://example.com/?a=1&b': 'http://example.com/?a=1&b',
        'http://example.com/?a&': 'http://example.com/?a',
        'http://example.com/?a=&': 'http://example.com/?a=',
        'http://example.com/?a=1&': 'http://example.com/?a=1',
    }

    authentication = {
        'http://example.com\\one\\two\\three': 'http://example.com/one/two/three',
        'http://:@example.com/': 'http://example.com/',
        'http://@example.com/': 'http://example.com/',
        'ftp://user:pass@ftp.foo.net/foo/bar': 'ftp://user:pass@ftp.foo.net/foo/bar',
        'http://USER:pass@www.Example.COM/foo/bar': 'http://USER:pass@www.example.com/foo/bar',
    }

    fragment = {
        'http://www.example.com#': 'http://www.example.com/',
        'http://www.example.com#frag': 'http://www.example.com/',
        'http://www.example.com/#': 'http://www.example.com/',
        'http://www.example.com/#frag': 'http://www.example.com/',
        'http://www.example.com/one/two#': 'http://www.example.com/one/two',
        'http://www.example.com/one/two#frag': 'http://www.example.com/one/two',
        'http://www.example.com/one/two/#frag': 'http://www.example.com/one/two/',
    }

    tld_dot = {
        'http://www.example.com./foo/bar.html': 'http://www.example.com/foo/bar.html',
        'http://www.example.com../foo/bar.html': 'http://www.example.com/foo/bar.html',
        'http://www.example.com  /foo/bar.html': 'http://www.example.com/foo/bar.html',
        'http://www.example.com.:81/foo': 'http://www.example.com:81/foo',
        'http://www.example.com./': 'http://www.example.com/',
        'http://www.example.com../': 'http://www.example.com/',
        'http://www.example.com.': 'http://www.example.com/',
        'http://www.example.com..': 'http://www.example.com/',
    }

    ends_with = {
        'http://www.example.com/one.': 'http://www.example.com/one',
        'http://www.example.com/one..': 'http://www.example.com/one',
        'http://www.example.com/one  ': 'http://www.example.com/one',
        'http://www.example.com/one/  ': 'http://www.example.com/one/',
        'http://www.example.com/one\r': 'http://www.example.com/one',
        'http://www.example.com/one\r\n': 'http://www.example.com/one',
        'http://www.example.com/one/\n': 'http://www.example.com/one/',
    }

    idna = {
        'http://例え.テスト/': 'http://xn--r8jz45g.xn--zckzah/',
    }
