from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.services.like_service import do_like, undo_like


class TestLikeService(TestCase):

    # def test_simple(self) -> None:
    #     # assert 옆에는 Expression, assert 옆이 false이면 예외 발생
    #     assert False

    def test_a_user_can_like_an_article(self) -> None:
        # X unit 계열 테스트 양식

        # Given 주어진 상황 -> 테스트 대상 정의
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When 테스트 실행 -> 테스트 상황, 함수 정의
        like = do_like(user.id, article.id)

        # for key, value in user.__dict__.items():
        #     print(key, value)
        #
        # print("reflection!")

        # Then 결과를 검증
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        # assert user_id == user_id
        self.assertEqual(article.id, like.article_id)

        # 테스트 코드는 최대한 분기, 반복 없이 단순하게 짜야한다

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test article")

        # Expect (when과 then을 같이 쓰고 싶은 경우)
        do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)

        # like1 = do_like(user.id, article.id)
        # try:
        #     like2 = do_like(user.id, article.id)
        # except Exception as e:
        #     print(e)

    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Expect
        with self.assertRaises(IntegrityError):
            do_like(invalid_user_id, article.id)

    def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
        # Given
        user = User.objects.create(name="test")
        invalid_article_id = 9988

        # Expect
        with self.assertRaises(IntegrityError):
            do_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        do_like(user.id, article.id)

        # Then
        article = Article.objects.get(id=article.id)

        self.assertEqual(1, article.like_set.count())

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = Like.objects.create(user_id=user.id, article_id=article.id)

        # When
        undo_like(user.id, article.id)

        # Then
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like.id)

    # def test_it_should_raise_exception_when_undo_like_which_does_not_exist(self) -> None:
    #     # Given
    #     user = User.objects.create(name="test")
    #     article = Article.objects.create(title="test_title")
    #
    #     # Expect
    #     with self.assertRaises(Like.DoesNotExist):
    #         undo_like(user.id, article.id)
