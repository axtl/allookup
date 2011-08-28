# allookup 

`allookup` attempts to find all known hostnames and IPv4 addresses for the hostname/IP argument(s) passed to it, and does so recursively on each answer until no more can be found.

It can be used stand-alone (as a shell utility), or as a Python module.

## Usage

### Shell

	$ allookup -h
	usage: allookup [-h] [-a] ADDRESS [ADDRESS ...]

    Queries for known hostnames/IP addresses of the given hostname/IP argument(s)

    positional arguments:
		ADDRESS     an address to lookup

    optional arguments:
		-h, --help  show this help message and exit
		-a, --arpa  Display .arpa addresses

### Python

	import allookup
	allookup.server_names(addr, show_arpa)
	"""Obtain all names that are associated with a given address.

    Keyword arguments:
    addr -- the address to explore (as IP or hostname)
    show_arpa -- include .arpa addresses (boolean, defaults to False)
    
    Returns a set containing the explored IPs and hostnames.
    """

## Output

	$ allookup mail.google.com
	mail.google.com is known as:

		74.125.53.83
		googlemail.l.google.com
		74.125.53.18
		74.125.53.19
		74.125.53.17
		pw-in-f18.1e100.net
		pw-in-f17.1e100.net
		mail.google.com
		pw-in-f83.1e100.net
		pw-in-f19.1e100.net
      
## License

[The MIT License](http://www.opensource.org/licenses/mit-license.html)
