from typing import Dict, Union, Any, List, Optional, Tuple

from db_manager.db_manager import DBManager


class SQLDataProvider:

	@staticmethod
	def sql_response_to_list(schema: List[str], response: Tuple[Tuple[Any]]) -> List[Dict[str, Any]]:
		return [dict(zip(schema, row_tuple)) for row_tuple in response]

	@staticmethod
	def get_user_by_login_and_password(login: str,
	                                   password: str,
	                                   config: Dict[str, Union[str, int]]) -> Optional[List[Dict[str, Any]]]:
		with DBManager(config) as cursor:

			_sql = """
			select u.login, u.password, ug.name
			from joom.user as u 
			join joom.user_group ug on
			u.group_name = ug.name
			where u.login='{}' and u.password='{}'
			""".format(login, password)

			cursor.execute(_sql)
			sql_result = cursor.fetchall()
			if sql_result:
				return SQLDataProvider.sql_response_to_list(['login', 'password', 'group'], sql_result)
			else:
				return None

	def get(self, request_name: str):
		pass
