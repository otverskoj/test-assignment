# import pytest
# from app._errors.user_does_not_exist_error import UserDoesNotExist
# from app.user.models.user import User
# from app.storage.user_db_repository import UserDBRepository
#
#
# def test_db_repo_create_and_get() -> None:
#     after_create = UserDBRepository().create(User(
#         **{
#             'first_name': 'Name',
#             'last_name': 'Familievich',
#             'middle_name': 'Patronymicievich'
#         }
#     ))
#
#     after_get = UserDBRepository().get_by_id(after_create.id_)
#
#     assert after_create == after_get
#
#
# @pytest.mark.usefixtures('insert_values_db')
# def test_db_repo_update() -> None:
#     id_ = 'aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa'
#     after_update = UserDBRepository().update(
#         id_,
#         User(
#             first_name='Test',
#             last_name='Testoviy',
#             middle_name='Testovich'
#         )
#     )
#
#     after_get = UserDBRepository().get_by_id(id_)
#
#     assert after_update == after_get
#
#
# @pytest.mark.usefixtures('insert_values_db')
# def test_db_repo_delete() -> None:
#     id_ = 'aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa'
#     UserDBRepository().delete(id_)
#
#     with pytest.raises(UserDoesNotExist):
#         UserDBRepository().get_by_id(id_)
