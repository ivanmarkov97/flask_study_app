from typing import Dict, Union

import pymysql


class DBManager:
	"""
	Класс для подключения к базе данных и выполнения запросов.
	Реализует поведение контекстного менеджера:
	with DBManager(...) as manager:
		do_something(...)
		....
	"""

	def __init__(self, config: Dict[str, Union[str, int]]) -> None:
		"""
		Инициализирует конктекстный менеджер конфигом для подклчюения к базе данных.

		Args:
			config - словарь с конфигом для подключения к БД.
		"""
		self.config = config

	def __enter__(self) -> pymysql.cursors.Cursor:
		"""
		Инициализрует соединение к базе данных и возвращет объект для выполнения запросов.

		Returns:
			Объект для выполнения запросов к БД.
		"""
		self.connection = pymysql.connect(**self.config)
		return self.connection.cursor()

	def __exit__(self, *args) -> None:
		"""
		Закрыывает соединение с БД и обрабатывает ошибки в случае их возникновения.

		Args:
			args - набор аргуметтов описывающий возникшие ошибки.
		"""
		self.connection.close()
