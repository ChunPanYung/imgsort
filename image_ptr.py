 
from PIL import Image

class ImagePtr:

  # static class variables
  _lst = [] # contains list of object ImagePtr

  def __init__(self, width, height, ptr):
    self.width = width
    self.height = height
    self.ptr = []
    self.ptr.extend(ptr)

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  def add_list(self, ptr):
    self.ptr.extend(ptr)

  # Static function
  # append image files into static class variable _lst
  # if they are image files
  @staticmethod
  def append(files):
    # check whether each file is img file, 
    # then get the width and height
    # put them in a list
    for f in files:
      img = Image.open(f)
      try: # verify whether it's image (loose verifcation)
        img.verify()
        # check if it's ImagePtr already exist
        length = len(ImagePtr._lst)
        if length != 0:
          # check each ImagePtr to see whether it matches the width and height
          for l in ImagePtr._lst:
            # if it's the same width and height
            if img.size == (l.get_width, l.get_height):
              l.add_list(f)
            # Otherwise create a new ImagePtr object on the list
            else:
              ImagePtr._append(f)
        # Otherwise create a new ImagePtr object on the list
        else:
          ImagePtr._append(f)
      except Exception:
        pass
  
  @staticmethod
  def _append(image):
    ImagePtr._lst.extend(ImagePtr(image.get_width, image.get_height, image))
