"""
is_ipv4_address(str): IPv4 address as argument to be checked
if it corresponds to RFC 791
returns boolean: True - correct, False - incorrect
"""


def is_ipv4_address(ip_addr):
    if '.' in ip_addr:
        ip_lst = ip_addr.split('.')
        if len(ip_lst) == 4:
            for octet in ip_lst:
                if not octet.isdigit() or len(octet) > 3 or int(octet) > 256:
                    return False
        else:
            return False
    else:
        return False
    return True


"""
is_ipv6_address(str): IPv6 address as argument to be checked 
if it corresponds to RFC 8200
returns boolean: True - correct, False - incorrect 
"""


def is_ipv6_address(ip_addr):
    if ':' in ip_addr and ip_addr.count('::') < 2:
        ip_lst = ip_addr.split(':')
        if len(ip_lst) < 9:
            for octet_dbl in ip_lst:
                if not octet_dbl:
                    continue
                if len(octet_dbl) > 4 or not octet_dbl.isalnum():
                    return False
                else:
                    octet_dbl = octet_dbl.upper()
                # TODO: IPv4 (pos) and use is_ipv4_address()
                for el in octet_dbl:
                    el = ord(el)
                    if el not in range(48, 58) and el not in range(65, 71):
                        return False
        else:
            return False
    else:
        return False
    return True


"""
is_email_domain_prt(str): e-mail address (domain part) as argument to be checked if it corresponds to
RFC 5322, RFC 5321, RFC 3696, RFC 6531
returns boolean: True - correct, False - incorrect 
"""


def is_email_domain_prt(email=''):
    domain_symbs = ['[', ']', '-', '.']
    domain_seq = email[email.rfind('@') + 1:]

    if len(domain_seq) < 1 or (domain_seq.startswith(domain_symbs[2]) or domain_seq.endswith(domain_symbs[2])) \
            or domain_seq.startswith(domain_symbs[3]) or domain_seq.endswith(domain_symbs[3]):
        return False
    if domain_seq.startswith(domain_symbs[0]) and domain_seq.endswith(domain_symbs[1]):
        if not is_ipv4_address(domain_seq[1:-1]):
            if not is_ipv6_address(domain_seq[1:-1]):
                return False
            else:
                return True
        else:
            return True

    domain_seq = domain_seq.upper()
    for i in domain_seq:
        i = ord(i)
        if i not in range(48, 58) and i not in range(65, 91) and i not in (45, 46):
            return False
    return True


"""
is_email_local_prt(str): e-mail address (local part) as argument to be checked if it corresponds to
RFC 5322, RFC 5321, RFC 3696, RFC 6531
returns boolean: True - correct, False - incorrect 
"""


def is_email_local_prt(email=''):
    in_quoters = ['..', '"', '(', ')', ',', ':', ';', '<', '>', '@', '[', '\\', ']']
    user_seq = email[:email.rfind('@')]

    if email.find('@') < 1 \
            or (user_seq.startswith('.') or user_seq.endswith('.')):
        return False
    if in_quoters[0] in user_seq \
            and (user_seq.find(in_quoters[1]) > user_seq.find(in_quoters[0])
                 or user_seq.find(in_quoters[0]) > user_seq.rfind(in_quoters[1])):
        return False

    for i in user_seq:
        if ord(i) not in range(32, 127):
            return False
        if i in in_quoters \
                and not(user_seq.find(in_quoters[1]) <= user_seq.find(i) <= user_seq.rfind(in_quoters[1])):
            return False
    return True


"""
is_email(str): e-mail address as argument to be checked if it corresponds to
RFC 5322, RFC 5321, RFC 3696, RFC 6531
returns boolean: True - is correct e-mail address, False - incorrect 
"""


def is_email(email):
    if is_email_local_prt(email) and is_email_domain_prt(email):
        return True
    else:
        return False


if __name__ == 'main':
    is_ipv4_address('')
    is_ipv6_address('')
    is_email_local_prt('')
    is_email_domain_prt('')
    is_email('')
