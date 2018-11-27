#by modifying the metaclass of a class, we can add feature to this class


class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		print "__new__ of ListMetaclass is called"
		attrs['add'] = lambda self, value:self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__ = ListMetaclass
	pass


L = MyList()
L.add(1)
print L