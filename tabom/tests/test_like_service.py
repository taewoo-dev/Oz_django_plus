from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


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
