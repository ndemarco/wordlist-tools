Wordlists are helpful in finding forgotten passwords. Many wordlists already exist. RockYou is probably the most commonly cited.
Tools like Hashcat and JohnTheRipper (JtR) include functions to manipulate wordlists to find passwords despite fairly ordinary manipulations.
Hashcat can combine lists of words, capitalize the first or last n letters, insert numbers, replace characters (like 'pa$$w0rd1' is really easy!).
No matter what password you use, if the password is eight or fewer characters long, it can be cracked in about a minute via a brute-force attack.
Adding a single character akes the password much more difficult.  

People who are more aware of password cracking tools know how to make more difficult passwords. The best password is a long random string consisting
of a large character set. Some passwords need to be remembered. For these, a difficult password can consist of:
* at least 12 characters, plus
* two or more words, plus
* one or more misspelled words, plus
* one or more capital letters embedded within the word, plus
* one or more numbers or symbols placed within the words, with
* none of the above following a pattern.  

For example: +eddy1bare:
* replaces 't' with +. This is predictable.
* Puts a single digit between the words. This is easily defeated with a brute force attack.
* Replaces the expected 'bear' with the homophone 'bare'. This is easily defeated with a brute force attack.  

A better memorable password: tedy4%4beaRr:
* 12 characters means a brute force
* two misspellings
* a number and symbol placed between misspelled words  

How wordlist-tools helps:
wordlist-tools includes utilities to manipulate a wordlist in a few ways:
1. Roll one or more capital letters through each word. 'audio' for one capital gives ['audio', 'Audio', 'aUdio', 'auDio', 'audIo', audiO'].
Two capitals adds these to the one capital list: ['AUdio', 'aUDio', 'auDIo', 'audIO'].
1. Generate all combinations of a word list. Combining the word list ['audio', 'video'] returns ['audiovideo', 'videoaudio'].
1. Roll one or more numbers through each word. Rolling one digit through the list ['audio'] returns ['1audio', 'a1udio', 'au1dio', 'aud1io', 'audi1o', \
'audio1', '2audio', 'a2udio', ...].
