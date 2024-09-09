from tabom.models import Like


# def do_like(user_id: int, article_id: int) -> Like:
#     return Like.do_like(user_id=user_id, article_id=article_id)
def do_like(user_id: int, article_id: int) -> Like:
    # 잘못된 방법: 단위테스트는 통과하지만 따닥 이슈 즉 여러 요청이 빠르게 들어올 경우 문제 발생
    # if Like.objects.filter(user_id=user_id, article_id=article_id).exists():
    #     raise Exception("이미 해당 사용자는 좋아요를 눌렀습니다")
    return Like.objects.create(user_id=user_id, article_id=article_id)
