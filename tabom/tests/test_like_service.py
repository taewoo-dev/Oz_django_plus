from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):

    # def test_simple(self) -> None:
    #     # assert 옆에는 Expression, assert 옆이 false이면 예외 발생
    #     assert False

    def test_a_user_can_like_an_article(self) -> None:
        # X unit 계열 테스트 양식

        # Given 주어진 상황에서
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When 테스트 실행
        like = do_like(user.id, article.id)

        # Then 결과를 검증
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        # assert user_id == user_id
        self.assertEqual(article.id, like.article_id)
