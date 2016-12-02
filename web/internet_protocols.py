# Source: http://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml
# http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
# See also: http://www.chebucto.ns.ca/~rakerman/port-table.html
# http://www.iss.net/security_center/advice/Exploits/Ports/default.htm
default_scheme_for_port = {
    # Permanent
    '647': 'acap',
    '1026': 'cap',
    '53': 'dns',
    '21': 'ftp',
    '70': 'gopher',
    '80': 'http',
    '443': 'https',
    '4569': 'iax',
    '1344': 'icap',
    '143': 'imap',  # IMAP4
    '220': 'imap',  # IMAP6
    '993': 'imap',  # IMAPs
    '631': 'ipp',
    #'5222': 'jabber',
    #'5269': 'jabber',
    '389': 'ldap',
    '636': 'ldap',  # LDAPs
    '2049': 'nfs',
    '119': 'nntp',  # NNTPs
    '563': 'nntp',  # NNTPs
    '109': 'pop',  # POP2
    '110': 'pop',  # POP3
    '995': 'pop',  # POP3s
    '554': 'rtsp',
    '322': 'rtsp',  # RTSPS
    '4190': 'sieve',
    '5060': 'sip',
    '5061': 'sips',
    '161': 'snmp',
    '1993': 'snmp',  # CISCO SNMP
    '5161': 'snmp',  # SNMP SSH
    '3427': 'snmp',  # SNMP WebSphere
    '10161': 'snmp',  # SNMP TLS
    '23': 'telnet',
    '107': 'telnet',  # remote telnet
    '69': 'tftp',
    '3713': 'tftp',  # TFTP over TLS
    '5222': 'xmpp',
    '5269': 'xmpp',
    # Provisional
    '548': 'afp',
    '5190': 'aim',
    '79': 'finger',
    '1234': 'git',
    # '1234': 'hg',
    '194': 'irc',
    '6660': 'irc',
    '6661': 'irc',
    '6662': 'irc',
    '6663': 'irc',
    '6664': 'irc',
    '6665': 'irc',
    '6666': 'irc',
    '6667': 'irc',
    '6668': 'irc',
    '6669': 'irc',
    '7000': 'irc',
    '873': 'rsync',
    '25': 'smtp',
    '465': 'smtp',  # SMTPs
    '587': 'smtp',  # SMTP email
    '115': 'sftp',  # Simple File Transfer Protocol (different than Secure File Transfer Protocol over SSH)
    '22': 'ssh',
    '773': 'submit',
    '2028': 'submit',
    '3690': 'svn',
    '191': 'prospero' # Historical
}
