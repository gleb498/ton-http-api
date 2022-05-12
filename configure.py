#!/usr/bin/env python3

import os
import sys


LOCAL_ENV = {
	'TON_API_CACHE_ENABLED': '0',
	'TON_API_LOGS_ENABLED': '0',
	'TON_API_LITE_SERVER_CONFIG': 'config/mainnet.json',
	'TON_API_ANALYTICS_PORT': '8081',
	'TON_API_ROOT_PATH': '/',
	'TON_API_ANALYTICS_ROOT_PATH': '/',
	'TON_API_FORWARDED_ALLOW_IPS': '',
	'TON_API_WEBSERVERS_WORKERS': '1',
	'TON_API_GET_METHODS_ENABLED': '1',
	'TON_API_JSON_RPC_ENABLED': '1',
	'TON_API_HTTP_PORT': '80',
	'TON_API_MONGODB_PORT': '27017'
}


def strtobool(val):
	if val.lower() in ['y', 'yes', 't', 'true', 'on', '1']:
		return True
	if val.lower() in ['n', 'no', 'f', 'false', 'off', '0']:
		return False
	raise ValueError(f"Invalid bool value {val}")

def main():
	default_env = LOCAL_ENV

	for var in default_env.keys():
		if os.getenv(var) != None:
			default_env[var] = os.getenv(var)

	compose_file = 'docker-compose.yaml'
	if strtobool(default_env['TON_API_CACHE_ENABLED']):
		compose_file += ':docker-compose.cache.yaml'
	if strtobool(default_env['TON_API_LOGS_ENABLED']):
		compose_file += ':docker-compose.logs.yaml'
	default_env['COMPOSE_FILE'] = compose_file

	env_content = ''
	for k, v in default_env.items():
		env_content += f'{k}={v}\n'

	with open(os.path.join(sys.path[0], ".env"), "w") as f:
	    f.write(env_content)

	print(".env file created.")

if __name__ == '__main__':
    main()
