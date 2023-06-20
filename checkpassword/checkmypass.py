# pip3 install requests
# allos us to request from the internet as if we are a browser
import requests
import hashlib # library that performs SHA1 hashing!
import sys

# A hash function returns a value of fixed length for each input
# idempotent is a technical way to say given an input the output will not change


# SHA1 gen of 'Let9me7in531!' is 300A69B3FEA040679261715EBC8456252630B64E
# This will use an api to get all the pwned passwords under the hash '300A6'
# On our end, we will check if the response includes one with the full hash
# K-anonymity works by only giving the first five chars of the hash.
# All the big companies do this!


def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	# gets the passwords that match the query
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fecthing {res.status_code}, check the api and try again')
	return res


def get_password_leaks_count(hashes, hashes_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hashes_to_check:
			return count
	return 0


def pwned_api_check(password):
	# Check password if it exists in api response
	sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first_5_char, tail = sha1_password[:5], sha1_password[5:]
	response = request_api_data(first_5_char)
	return get_password_leaks_count(response, tail)


def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'The password {password} was found {count} times')
		else:
			print(f'{password} was not found. Carry on!')
	return 'done!'


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))