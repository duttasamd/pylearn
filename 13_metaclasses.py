class Base:
    def foo(self):
        return 'foo'


assert hasattr(Base, 'foo') # use this before using the members of a class writen by someone else.
# This is important because we may not have control over the library classes.
# This is to stop our code from breaking if our library class changes.
# We can catch the change before we try to use the method.


class Derived(Base):
    def bar(self):
        return self.foo()


# ===========================================================================
# The other way round.
# Ensure that the Derived classes have a bar method. This is much like interfaces.

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'bar' not in body and name != 'Base':
            raise TypeError("Bad User Method")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()


# Does not throw an error
class Derived(Base):
    def bar(self):
        return 'bar'


# Throws an error
# class Derived_E(Base):
#     pass

# ========================================================================

# Metaclasses are clumsy. In python3 we have an easier way to hook into the subclass creation code.

class Base():
    def foo(self):
        return self.bar()

    def __init_subclass__(cls, **kwargs):
        assert hasattr(cls, 'bar')


# Does not throw an error
class Derived(Base):
    def bar(self):
        return 'bar'


# Throws an error
class Derived_E(Base):
    pass

