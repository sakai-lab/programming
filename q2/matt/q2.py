import re
def read_data():
    """
    >>> d = read_data()
    >>> d["sato"]["height"]
    172.5
    >>> d["sato"]["weight"]
    66.5
    """

    data = []
    with open("../data.txt") as f:
        data = [line.strip().split(",") for line in f.readlines()]
    return {name:{"weight":float(weight), "height":float(height)}
            for name, height, weight in data}

def get_bmi(name):
    """
    >>> bmi = get_bmi("sato")
    >>> abs(bmi - 0.002224743) < 1E-3
    True
    """
    data = read_data()
    if name not in data:
        print "unexpected input"
        return
    person = data[name]
    height = person["height"]
    weight = person["weight"]
    return weight / (height * height)

def is_email_addr(addr):
    """
    >>> is_email_addr("asdf@aol.com")
    True
    >>> is_email_addr("asdf@adsf@adsf")
    False
    >>> is_email_addr("sadf.asdf")
    False
    >>> is_email_addr("asdf@wa.we.fe.o")
    True
    """
    # see http://www.w3.org/TR/html5/forms.html#valid-e-mail-address
    pattern = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
                         "@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
                         "(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    match = re.match(pattern, addr)
    return match is not None
