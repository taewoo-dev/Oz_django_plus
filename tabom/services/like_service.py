from tabom.models import Like


# def do_like(user_id: int, article_id: int) -> Like:
#     return Like.do_like(user_id=user_id, article_id=article_id)
def do_like(user_id: int, article_id: int) -> Like:
    # 잘못된 방법: 단위테스트는 통과하지만 따닥 이슈 즉 여러 요청이 빠르게 들어올 경우 문제 발생
    # if Like.objects.filter(user_id=user_id, article_id=article_id).exists():
    #     raise Exception("이미 해당 사용자는 좋아요를 눌렀습니다")
    return Like.objects.create(user_id=user_id, article_id=article_id)


def undo_like(user_id: int, article_id: int) -> None:
    Like.objects.filter(user_id=user_id, article_id=article_id).delete()
    # like.delete()
    # 이렇게 하면 쿼리를 두번 날려야한다. 네트워크를 거쳐가는 쿼리라 매우 큰 낭
    # likes = list(Like.objects.filter(id__in=[1,2,3]))

    # get, filter의 차이
    # like는 Like 객체
    # like = Like.objects.get(user_id=user_id, article_id=article_id)
    # # like2는 쿼리셋
    # # 쿼리셋은 진짜로 실행되야하는 시점까지 쿼리를 미룬다 : lazy <-> eager
    # # list로 감싸면 바로 쿼리가 실행되어 list[Like]
    # like2 = Like.objects.filter(user_id=user_id, article_id=article_id)
    # print(like, like2)
