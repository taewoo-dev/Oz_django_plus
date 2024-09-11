from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext

from tabom.models import Article, Like, User
from tabom.services.article_service import get_an_article, get_article_list


class TestArticleService(TestCase):
    def test_you_can_get_an_article_by_id(self) -> None:
        # Given
        title = "test_title"
        article = Article.objects.create(title=title)

        # When
        result_article = get_an_article(article.id)

        # Then
        self.assertEqual(article.id, result_article.id)
        self.assertEqual(title, result_article.title)

    def test_it_should_raise_exception_when_article_does_not_exist(self) -> None:
        # Given
        invalid_article_id = 9988

        # Expect
        with self.assertRaises(Article.DoesNotExist):
            get_an_article(invalid_article_id)

    def test_get_article_list_should_prefetch_likes(self) -> None:
        # Given
        user = User.objects.create(name="test_user")
        # test라 for문, 한방쿼리는 bulk_create
        articles = [Article.objects.create(title=f"test_article_{i}") for i in range(1, 21)]
        Like.objects.create(user_id=user.id, article_id=articles[-1].id)

        # When
        result_articles = get_article_list(0, 10)
        result_counts = [a.like_set.count() for a in result_articles]

        with self.assertNumQueries(2):  # N+1 문제를 assertNumQuerise를 이용해서 잡을 수 있다
            # 장고 admin과 pagenator를 사용할 때 where절 없는 sql문을 날리기에 대용량 쿼리를 날리 시에는 조심헤야한다
            # When
            result_articles = get_article_list(0, 10)
            result_counts = [a.like_set.count() for a in result_articles]

            # Then
            self.assertEqual(len(result_articles), 10)
            self.assertEqual(1, result_counts[0])
            self.assertEqual(
                [a.id for a in reversed(articles[10:21])],
                [a.id for a in result_articles],
            )

        # Then
        # 간헐적 테스트 실패 -> 비교가 목적이나 순서가 다른 경우에 문제가 생긴 -> set으로 만들어 순서를 없엔다
