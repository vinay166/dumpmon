import re

regexes = {
	'email' : re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', re.I),
	#'ssn' : re.compile(r'\d{3}-?\d{2}-?\d{4}'),
	'hash32' : re.compile(r'[A-F0-9]{32}', re.I),
	'FFF' : re.compile(r'(?<!color:\s)(?:#FFF)|(?:FBI\s*Friday)', re.I), # will need to work on this to not match CSS
	'lulz' : re.compile(r'(?:lulzsec)|(?:antisec)', re.I),
	'cisco_hash' : re.compile(r'enable\s+secret', re.I),
	'cisco_pass' : re.compile(r'enable\s+password', re.I),
	'google_api' : re.compile(r'(AIza.{35})', re.I),
	'db_keywords' : [
					re.compile(r'(((?:customers?)|(?:email)|(?:users?)|(?:members?)|(?:accounts?)[-_|/\s]?(?:address)|(?:names?)|(?:ids?[^")])\W))', re.I),
					re.compile(r'(?:\btarget)|(?:\bsite)\s*?:?\s*?((?:[a-z][\w-]+:/{1,3})?(?:[-\w\s_]\.)*)', re.I), # very basic URL check - may be improved later
					re.compile(r'((?:my\s?sql[^i_])|(?:sql\s*server))', re.I),
					re.compile(r'((?:data[-_\s]*base)|(?:\Wdb))', re.I), #added the non-word char before db.. we'll see if that helps
					re.compile(r'(table\s*?:)', re.I)
				],
	'blacklist' : [	# I was hoping to not have to make a blacklist,
					re.compile(r'(?:select\s+.*?from)|(?:join)|(?:declare\s+.*?\s+as\s+)', re.I), # SQL
					re.compile(r'((?:define\(.*?\))|(?:require_once\(.*?\)))', re.I), # PHP
					re.compile(r'(function.*?\(.*?\))', re.I),
					re.compile(r'Configuration\.Factory', re.I),
					re.compile(r'(?:border)|(?:background)-color)', re.I),
					re.compile(r'Traceback \(most recent call last\)', re.I)
				],
	'white_list' : [ # This is for regex that is almost sure to be in database leaks
					re.compile(r'[-|+\n]+?\s*(?:table)|(?:column)|(?:customers?)|(?:email)|(?:users?)|(?:members?)|(?:accounts?)[-_|/\s]?(?:address)|(?:names?)|(?:ids?[^")])\s*[-|]', re.I)
				]
}