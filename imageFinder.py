import glob

class ImageStorage():
    def home_image(self):
        pass
    
    def one_image(self):
        pass
    
    def two_image(self):
        pass
    
    def three_image(self):
        pass
    
    def four_image(self):
        pass
    
    def contact_image(self):
        pass

class DictStorage(ImageStorage):
    
    __images = {}
    
    def __init__(self):
        imageFile = glob.glob("static/*")
        
        for photo in imageFile:
            self.__images[photo + "photo"] = photo
    
    def home_image(self):
        return self.__images["cs.jpg" + "photo"]
    
    def one_image(self):
        return self.__images["one.png" + "photo"]
    
    def two_image(self):
        return self.__images["two.png" + "photo"]
    
    def three_image(self):
        return self.__images["three.jpg" + "photo"]
    
    def four_image(self):
        return self.__images["four.png" + "photo"]
    
    def contact_image(self):
        return self.__images["contacts.png" + "photo"]


class ListStorage(ImageStorage):
    
    __images = []
    
    def __init__(self):
        imageFile = glob.glob("static/*")
        
        for photo in imageFile:
            self.__images.append(photo[7:])
    
    def home_image(self):
        print(self.__images[1])
        return self.__images[1]
    
    def one_image(self):
        return self.__images[3]
    
    def two_image(self):
        return self.__images[5]
    
    def three_image(self):
        return self.__images[4]
    
    def four_image(self):
        return self.__images[2]
    
    def contact_image(self):
        return self.__images[0]


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()