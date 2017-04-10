class Car(object):
    """
    Audi OOOO
    """

c = Car()
setattr(c, "model", "RS3")

print(c.model)
print(c.__doc__)

