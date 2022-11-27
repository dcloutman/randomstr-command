# `randomstr`: A command line password generator.
A command line tool for generating **secure random passwords** and other cryptographically secure random strings.

This utility *does not* use the standard Python `random()` function, as the results of that function are not sufficiently random for producing difficult to produce passwords. Modifying this code to use `random()` will render `randomstr` ineffective.

## Requirements to Run `randomstr`
`randomstr` is written in Python 3. You will need a binary release of Python 3 to use this utility. The shebang assumes that you have the command `python3` available in your shell's path.

Additionally, there are dependencies on the following libraries:
* Click, a command-line framework for Python
* Secrets, a cryptographic library

You will most likely want to install these features globally. Alternatively, you may use the requirements.txt file to set up a virtual environment, though this will make using the library less convenient.

# Usage Hints

Running `randomstr --help` will display the built-in help for the utility.

A standard list of commonly forbidden characters in passwords is included in the built-in disallowed characters list. You can increase the complexity of your random strings by passing an empty `--no` option. However, this will potentially cause some services to reject your password / secret as some developers wrongly believe disallowing these characters will protect them against SQL injection or XSS attacks.

If you need to add additional characters to the default disallow list, use the `--also-no` option and pass a string of characters you wish to disallow. These characters will be added to the disallow list.

Basic usage of this utility generates a randomized string of a length specified by the user.

```bash
randomstr 12
```

However, you may make your password a randomized length by using the `--min-length` and `--max-length` options to create an inclusive range of possible string lengths.

```bash
randomstr --min-length 12 --max-length 22
```

# Caveat Non Emptor
No password will give you 100% protection against brute force attacks, but it is hoped that this utility will decrease the probability of having your secured accounts hacked through social engineering, guessing, and brute force attacks. That being said, this is Free software, so there is no actual or implied warranty. If you find a problem, please report it as a bug in Github.


*v0.0.3*, (c)2022 David Cloutman under MIT License.