import json
import yaml

from typing import Dict, Optional, Any

from flask import session


def config_from_file(path: str, type: Optional[str] = None) -> Dict[str, str]:
	if type is None:
		type = path.split('.')[-1]
	if type not in ['json', 'yaml', 'yml', 'txt']:
		raise ValueError('file type not in ')
	if type == 'json':
		with open(path, 'r') as f:
			return json.loads(f.read())
	elif type in ['yml', 'yaml']:
		return yaml.load(open(path, 'r'), Loader=yaml.FullLoader)
	else:
		with open(path, 'r') as f:
			data = {}
			for line in f.readlines():
				key, value = line.split('=')
				value = value.replace('\n', '').strip()
				data[key] = value
			return data


def write_session(data: Dict[str, Any]) -> None:
	for key in data:
		session[key] = data[key]


def clear_session() -> None:
	session.clear()
