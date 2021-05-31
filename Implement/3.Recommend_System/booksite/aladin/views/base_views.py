from django.http import HttpResponse
from django.shortcuts import render, redirect
from aladin.models import bookSnapShot
from django.urls import reverse
from django.views.generic import View
from aladin.views.recommend_views import *
from datetime import datetime



class BookPosition:
    pos = 0
    def get(self):
        return self.pos
    def set(self,pos):
        self.pos = pos
class_p = BookPosition()
p = class_p.get()

class Selector:
    def __init__(self,p):
        self.p = p
    def selectBook(self):
        booklist = bookSnapShot.objects.order_by('id')[self.p:self.p+5]
        return booklist

class ButtonKey:
    def __init__(self,key):
        self.key = key
    def isLeftArrow(self):
        if self.key == "leftArrow":
            return True
        else:
            return False
    def isRightArrow(self):
        if self.key == "rightArrow":
            return True
        else:
            return False

    def isLeftRefresh(self):
        if self.key == "leftRefresh":
            return True
        else:
            return False
    def isRightRefresh(self):
        if self.key == "rightRefresh":
            return True
        else:
            return False

class ButtonCtrl:
    button = ""
    def __init__(self,p):
        self.p = p
    def sendKey(self,button):
        self.button = button
        k = ButtonKey(button)
        if k.isLeftArrow():
            self.p -= 5
        elif k.isRightArrow():
            self.p += 5
        elif k.isLeftRefresh():
            self.p -= 20
        elif k.isRightRefresh():
            self.p += 20
        if self.p <0:
                self.p = 0
        elif self.p > 60:
            self.p=0
        return self.p

''' ========================================= '''


class Search(View):
    def get(self, req):
        return HttpResponse('<h1>검색 페이지로 이동</h1>')


class Detailbook(View):
    def get(self, req, id=''):
        # 로그인 파트에서 쿠키로 저장한 customerID
        customerID = KeyStorage().loadCustomerID()
        log = id+',3'
        book_id, rating = L.filterLog(log)
        logDB.recordData(customerID, book_id, rating)  # get log
        return HttpResponse('<h2>Book ID : '+ id +" 's detail page</h2>")


class Logger:
    def filterLog(self,log):
        # user_id 빼고 book_id, rating 순으로 자르기
        log_list = log.split(',')
        book_id = log_list[0]
        rating = log_list[1]
        return book_id, rating


class KeyStorage:
    def loadCustomerID(self):
        customerID = "3001" # 로그인 파트에서 쿠키로 저장한 customerID
        return customerID

''' ========================================= '''

def change(req):
    if req.session.get('p'):
        p = req.session['p']
    else:
        req.session['p']=0
        p=0
    p = ButtonCtrl(p).sendKey(req.POST['button'])
    req.session['p']=p
    print(p)

    S = Selector(p)
    booklist = S.selectBook()
    print(booklist)
    context = {
        "book1":booklist[0],
        "book2":booklist[1],
        "book3":booklist[2],
        "book4":booklist[3],
        "book5":booklist[4]
    }
    return render(req, "main.html", context=context)

    #return redirect('main')

''' ========================================= '''
userID = int(KeyStorage().loadCustomerID())  # 키 값 받아서 하기. - API

bookDB = BookDBconnection()  # connect to books.csv
logDB = LogDBconnection()  # connect to log DB

bookDB.CustomerID(userID)
logDB.CustomerID(userID)

bookDB.bookData()  # preprocessing book data
logDB.usersData()  # preprocessing log data

bookSnapshot = BookSnapshot()
recommender = Recommendation(bookDB.book_data, logDB.log_data)

# 05.29 추가
L = Logger()

# Create your views here.
def main(req):
    if req.session.get('p'):
        p = req.session['p']
    else:
        req.session['p']=0
        p=0

# start recommender -----------------------------------------------------------

    # load the updated book data
    if bookDB.initAccess == None or bookDB.isUpdated == True:
        bookDB.updated_book()
        bookDB.bookData()

    # load the updated log data
    logDB.updated_log()

    # run recommendation
    recommender.updated_data(bookDB.book_data, logDB.log_data)
    already_rated = recommender.runRecommendation(userID)
    logDB.timestamp = datetime.now()  # return the end of the recommend time

    # make book snapshot
    bookSnapshot.generateRecommendationList(recommender.recommendList)
# -------------------------------------------------------------------------------------
    # print("Successfully recommended")

    S = Selector(p)

    booklist = S.selectBook()
    context = {
        "book1":booklist[0],
        "book2":booklist[1],
        "book3":booklist[2],
        "book4":booklist[3],
        "book5":booklist[4]
    }
    return render(req, "main.html", context=context)

