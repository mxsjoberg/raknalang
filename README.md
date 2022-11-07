# raknalang (räknalang)

This is a simple domain-specific programming language to do basic arithmetic in natural language.

## Getting started

1. First, `$ python main.py --lang` to start interpreter (lang: swedish, english)
	- `--test` to run tests
		```bash
		$ python main.py --swedish --test
		Running raknalang interpreter...
		 LANGUAGE: SWEDISH
		 Running tests...
		  ett plus ett => 2  OK
		  två minus tre => -1  OK
		  fem myror är fler än fyra elefanter => Sant  OK
		  två lasbilar är färre än en bil => Falskt  OK
		  två äpplen delat på två personer => 1  OK
		  tre päron delat med två personer => 1  OK
		  en glass delad med fyra personer => 0  OK
		  ett plus ett är större än tre minus två => Sant  OK
		  fyra ben gånger två kor => 8  OK
		  två äpplen plus fyra päron är mer än ett päron => Sant  OK
		  två kronor gånger ett är mindre än en krona gånger fyra => Sant  OK
		  två gånger två gånger två => 8  OK
		  ett gånger två minus två gånger fyra => -6  OK
		 Tests done.
		Exiting...
		```

	- `--debug` to show output from lexer and parser
		```bash
		$ python main.py --english --debug
		Running raknalang interpreter...
		 LANGUAGE: ENGLISH
		 Type 'q' + ENTER to exit.
		  DEBUG MODE
		  > one plus two minus three
		  lexer (tokens): [1, '+', 2, '-', 3]
		  parser (AST): {'node': '-', 'children': [{'node': '+', 'children': [1, 2]}, {'node': None, 'children': [3]}]}
		  0
		  >
		```

2. then, enter some calculation in natural language
	- e.g. enter `ett gånger två minus två gånger fyra` + ENTER gives result `-6` (`1 * 2 - 2 * 4`)
		```bash
		$ python main.py --swedish
		Running raknalang interpreter...
		 LANGUAGE: SWEDISH
		 Type 'q' + ENTER to exit.
		  > ett gånger två minus två gånger fyra
		  -6
		  >
		```

3. finally, enter 'q' + ENTER to exit.

## TODO

- use any number as input, see [https://michaelsjoeberg.com/programming/python/project-euler-problems/number-letter-counts](https://michaelsjoeberg.com/programming/python/project-euler-problems/number-letter-counts)

## Operators

| symbol | operator     | swedish       	| english 					  |
| :----: | :----------- | :----------------	| :-------------------------- |
| --     | COMMENT      |  					|   						  |
| +      | PLUS         | plus          	| plus, add, added  		  |
| -      | MINUS        | minus          	| minus, subtract, subtracted |
| >      | GREATER THAN | fler, mer, större | greater, more, larger  	  |
| <      | LESS THAN 	| färre, mindre 	| less, smaller 			  |
| /      | DIVIDE       | delat, delad      | divided, split 			  |
| *      | MULTIPLY     | gånger 	        | times, multiply, multiplied |

## Examples

**English**

```
> one plus one
2

> two minus three
-1

> five ants are more than four elephants
True

> two apples split on two people
1

> three pears divided with two people
1

> one times two minus two times four
-6
```

**Swedish**
	
```
> ett plus ett
2

> två minus tre
-1

> fem myror är fler än fyra elefanter
Sant

> två lasbilar är färre än en bil
Falskt

> tre päron delat med två personer
1

> ett plus ett är större än tre minus två
Sant
```
