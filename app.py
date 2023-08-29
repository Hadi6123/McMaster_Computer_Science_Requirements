from flask import Flask, render_template, url_for
from stragety import *
from imageFinder import *


app = Flask(__name__)

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    
    __method = None
    __imageStorage = None
    
    def __init__(self, imageStorage=None):
        print('Loading database')
        self.__method = YearOneStrategy()
        self.__imageStorage = imageStorage
    
    def getFruitHeaders(self):
        headers = ['Course Code', 'Course Name', 'Description', 'Requirements', 'Units']
        
        return headers
    
    def getFruitList(self):
        return self.__method.getData()
    
    def set_method(self, level):
        if (level == 1):
            self.__method = YearOneStrategy()
        elif (level == 2):
            self.__method = YearTwoStrategy()
        elif (level == 3):
            self.__method = YearThreeStrategy()
        else:
            self.__method = YearFourStrategy()
    
    def get_image(self, page):
        
        photo = None
        
        if (page == 1):
            photo = "static/"+self.__imageStorage.home_image()
        elif (page == 2):
            photo = self.__imageStorage.one_image()
        elif (page == 3):
            photo = self.__imageStorage.two_image()
        elif (page == 4):
            photo = self.__imageStorage.three_image()
        elif (page == 5):
            photo = self.__imageStorage.four_image()
        else:
            photo = self.__imageStorage.contact_image()
        
        return photo

@app.route('/')
def home():
    
    database = Database(ListStorage())
    
    
    return render_template(
        'index.html', result=database.get_image(1)    )

@app.route('/yearone/')
def yearone():

    database = Database(ListStorage())
    database.set_method(1)
    
    print(database.get_image(2))

    return render_template(
        'course.html',
        headers=database.getFruitHeaders(),
        tableData=database.getFruitList(),
        dataToRender="Year One Required CS Courses",
        result=database.get_image(2)  
    )

@app.route('/yeartwo/')
def yeartwo():

    database = Database(ListStorage())
    database.set_method(2)

    return render_template(
        'course.html',
        headers=database.getFruitHeaders(),
        tableData=database.getFruitList(),
        dataToRender="Year Two Required CS Courses",
        result=database.get_image(3)  
    )
    
@app.route('/yearthree/')
def yearthree():

    database = Database(ListStorage())
    database.set_method(3)

    return render_template(
        'course.html',
        headers=database.getFruitHeaders(),
        tableData=database.getFruitList(),
        dataToRender="Year Three Required CS Courses",
        result=database.get_image(4)  
    )

@app.route('/yearfour/')
def yearfour():

    database = Database(ListStorage())
    database.set_method(4)

    return render_template(
        'course.html',
        headers=database.getFruitHeaders(),
        tableData=database.getFruitList(),
        dataToRender="Year Four Required CS Courses",
        result=database.get_image(5)  
    )

if __name__ == '__main__':
    app.run()