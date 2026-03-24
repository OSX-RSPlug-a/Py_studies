import pytest


class DescriptorFace:
	def __get__(self, instance: object | None, owner: type):
		pass
		
		
	def __set__(self, instance: object, value: int):
		pass


#tests
class TestHost:
    """A dummy class to host the descriptor for testing."""
    face = DescriptorFace()

def test_descriptor_get_on_instance():
    host = TestHost()
    # This triggers DescriptorFace.__get__
    assert host.face == "getting value"

def test_descriptor_get_on_class():
    # When accessed via the class, 'instance' is None
    # Usually, descriptors return themselves in this case
    assert isinstance(TestHost.face, DescriptorFace)

def test_descriptor_set():
    host = TestHost()
    host.face = 42  # Triggers DescriptorFace.__set__
    
    # Verify the side effect (depending on your __set__ logic)
    assert host._face_value == 42