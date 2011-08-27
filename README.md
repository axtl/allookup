# allookup 

`allookup` attempts to find all known hostnames and IPv4 addresses for the hostname/IP argument(s) passed to it, and does so recursively on each answer until no more can be found.

## Usage

	allookup -a mail.google.com -a 127.0.0.1

## Output

* `allookup`:

		$ allookup.py -a mail.google.com
		mail.google.com is known as:

            74.125.53.83
            googlemail.l.google.com
            74.125.53.18
            74.125.53.19
            74.125.53.17
            pw-in-f18.1e100.net
            17.53.125.74.in-addr.arpa
            pw-in-f17.1e100.net
            mail.google.com
            pw-in-f83.1e100.net
            pw-in-f19.1e100.net
            83.53.125.74.in-addr.arpa
            19.53.125.74.in-addr.arpa
            18.53.125.74.in-addr.arpa
* `host`:

		$ host mail.google.com
		mail.google.com is an alias for googlemail.l.google.com.
		googlemail.l.google.com has address 74.125.127.19
		googlemail.l.google.com has address 74.125.127.83
		googlemail.l.google.com has address 74.125.127.17
		googlemail.l.google.com has address 74.125.127.18

* `nslookup`:

		$ nslookup mail.google.com
		Server:		198.162.52.58
		Address:	198.162.52.58#53
		
		Non-authoritative answer:
		mail.google.com	canonical name = googlemail.l.google.com.
		Name:	googlemail.l.google.com
		Address: 74.125.127.83
		Name:	googlemail.l.google.com
		Address: 74.125.127.17
		Name:	googlemail.l.google.com
		Address: 74.125.127.18
		Name:	googlemail.l.google.com
		Address: 74.125.127.19
