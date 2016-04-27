import re
def q1(string="I am an real sakai lab student"):
    """
    >>> q1()
    'IAARSLS'
    """
    return "".join(w[0].capitalize() for w in re.split(r"\s+", string))


def q2(ip_input):
    """
    >>> q2("1.1.1.1")
    True
    >>> q2("1.2.3..5")
    False
    >>> q2("1234.123.123.123")
    False
    """
    return (ip_input.count(".")==3 and
            len(filter(lambda x:0 <= int(x) <= 255, ip_input.split("."))) == 4)

def q3(surname_input):
    """
    >>> q3("sakai")
    'tetsuya'
    """
    return (surname_input
            .replace("sakai","tetsuya")
            .replace("nakajima","tatsuo")
            .replace("washizaki","hironor"))
