from django.shortcuts import render
from ..models import bookSnapShot, LOG_DB
from datetime import datetime
from django.utils import timezone

from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series, DataFrame

import numpy as np
import warnings
warnings.filterwarnings("ignore")

class BookDBconnection:
    def __init__(self):
        self.book_data = pd.read_csv('aladin/views/books.csv')
        self.initAccess = 1 # None
        self.isUpdated = False # True
        self.customer_id = None

    def CustomerID(self, key):  # 고객 아이디 저장
        self.customer_id = key

    def updated_book(self):  # 업데이트 된 책 로드
        self.book_data = pd.read_csv('aladin/views/books.csv')

    def bookData(self):  # 책 데이터 preprocessing
        self.book_data.drop('id', axis=1, inplace=True)
        self.book_data.drop('best_book_id', axis=1, inplace=True)
        self.book_data.drop('work_id', axis=1, inplace=True)
        self.book_data.drop('books_count', axis=1, inplace=True)
        self.book_data.drop('isbn', axis=1, inplace=True)
        self.book_data.drop('isbn13', axis=1, inplace=True)
        self.book_data.drop('original_publication_year', axis=1, inplace=True)
        self.book_data.drop('original_title', axis=1, inplace=True)
        self.book_data.drop('language_code', axis=1, inplace=True)
        self.book_data.drop('average_rating', axis=1, inplace=True)
        self.book_data.drop('ratings_count', axis=1, inplace=True)
        self.book_data.drop('work_ratings_count', axis=1, inplace=True)
        self.book_data.drop('work_text_reviews_count', axis=1, inplace=True)
        self.book_data.drop('ratings_1', axis=1, inplace=True)
        self.book_data.drop('ratings_2', axis=1, inplace=True)
        self.book_data.drop('ratings_3', axis=1, inplace=True)
        self.book_data.drop('ratings_4', axis=1, inplace=True)
        self.book_data.drop('ratings_5', axis=1, inplace=True)
        self.book_data.drop('image_url', axis=1, inplace=True)

        return self.book_data


class LogDBconnection:
    def __init__(self):
        self.log_data = pd.DataFrame()
        self.timestamp = datetime.now()
        self.customer_id = None

    def CustomerID(self, key):   # 고객 아이디 저장
        self.customer_id = key

    def compare_Timestamp(self):  # 업데이트 된 로그 데이터 로드
        print("추천 시간", self.timestamp)
        new_log = LOG_DB.objects.filter(timestamp__gt=self.timestamp)
        print("데이터 시간", new_log)
        if new_log.exists():
            new_log = new_log.values('user_id', 'book_id', 'rating')
            df_log = pd.DataFrame(list(new_log))
            df_log = df_log.drop_duplicates(['user_id', 'book_id'], keep='last')
        else:
            df_log = pd.DataFrame()
        return df_log

    def updated_log(self):  # 마지막 추천 이후 추가된 로그
        df_log = self.compare_Timestamp()
        self.log_data = self.log_data.append(df_log)
        print("여깄고")

    def usersData(self):  # 로그 데이터 로드
        new_log = LOG_DB.objects.all().values('user_id', 'book_id', 'rating').order_by("timestamp")
        df_log = pd.DataFrame(list(new_log), columns=['user_id', 'book_id', 'rating'])

        self.log_data = self.log_data.append(df_log)
        self.log_data = self.log_data.drop_duplicates(['user_id', 'book_id'], keep='first')


    def recordData(self,user_id, book_id, rating):  # 로그 데이터 수집
        LOG_DB(user_id=user_id, book_id=book_id, rating=rating).save()
        print(LOG_DB.objects.count())


class Recommendation:

    def __init__(self, ori_books_df, ori_log_df):
        self.recommendList = pd.DataFrame(columns=['book_id', 'authors', 'title', 'Predictions'])
        self.book_data = ori_books_df
        self.log_data = ori_log_df

    def updated_data(self, ori_books_df, ori_log_df):  # 업데이트 된 데이터 로드
        self.book_data = ori_books_df
        self.log_data = ori_log_df

    def runRecommendation(self, user_Id, num_recommendations=60):  # 추천 알고리즘
        ori_books_df = self.book_data                              # - collaborative filtering
        ori_log_df = self.log_data                                 # - Matrix Factorization
                                                                   # 사용자별 추천
        user_book_log = ori_log_df.pivot(index='user_id', columns='book_id', values='rating').fillna(0)
        matrix = user_book_log.values

        # Matrix Factorization
        user_log_mean = np.mean(matrix, axis=1)
        matrix_user_mean = matrix - user_log_mean.reshape(-1, 1)

        U, sigma, Vt = svds(matrix_user_mean, k=12)
        sigma = np.diag(sigma)

        svd_user_predicted_log = np.dot(np.dot(U, sigma), Vt) + user_log_mean.reshape(-1, 1)
        df_svd_preds = pd.DataFrame(svd_user_predicted_log, columns=user_book_log.columns)

        # run recommendation
        user_row_number = user_Id - 1

        sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)
        user_data = ori_log_df[ori_log_df.user_id == user_Id]
        user_history = user_data.merge(ori_books_df, on='book_id').sort_values(['rating'], ascending=False)

        recommendations = ori_books_df[~ori_books_df['book_id'].isin(user_history['book_id'])]
        recommendations['book_id'] = recommendations['book_id'].astype("str")
        a = pd.DataFrame(sorted_user_predictions).reset_index()
        a['book_id'] = a['book_id'].astype("str")
        recommendations = recommendations.merge(a, on='book_id')
        recommendations = recommendations.rename(columns={user_row_number: 'Predictions'}).sort_values('Predictions',ascending=False).iloc[:num_recommendations, :]

        self.recommendList = recommendations

        return user_history


class BookSnapshot:

    def __init__(self):
        self.book_list = pd.DataFrame(columns=['book_id', 'authors', 'title', 'small_image_url', 'Predictions'])
        self.usedRecommendationAlgorithm = "collaborative filtering"

    def generateRecommendationList(self, recommended_books):  # 북 스냅샷 생성
        self.book_list = recommended_books
        book_idx = self.book_list.index
        booksnapshot = bookSnapShot.objects.all()
        booksnapshot.delete()

        print(book_idx)
        for idx in book_idx:
            book_name = self.book_list.loc[idx, 'title']
            book_author = self.book_list.loc[idx, 'authors']
            book_image = self.book_list.loc[idx, 'small_image_url']
            bookSnapShot(name=book_name, author=book_author, image=book_image).save()

        return book_idx