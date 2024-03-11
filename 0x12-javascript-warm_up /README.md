0x12. JavaScript - Warm up
==========================

-   By Guillaume

Background Context
------------------

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

-   Scripting (same as we did with Python)
-   Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg)

Resources
---------

**Read or watch**:

-   [Writing JavaScript Code](https://alx-intranet.hbtn.io/rltoken/3HLjEesLsmyWfRUWnxgUGg "Writing JavaScript Code")
-   [Variables](https://alx-intranet.hbtn.io/rltoken/zgOWmcpVLZFEmFlmuwayyg "Variables")
-   [Data Types](https://alx-intranet.hbtn.io/rltoken/VPd6JWaLrwOBzjAeXNAEqg "Data Types")
-   [Operators](https://alx-intranet.hbtn.io/rltoken/3HLjEesLsmyWfRUWnxgUGg "Operators")
-   [Operator Precedence](https://alx-intranet.hbtn.io/rltoken/PHtcJJk30gBNmlFQ9R4RVg "Operator Precedence")
-   [Controlling Program Flow](https://alx-intranet.hbtn.io/rltoken/tsreKcNh_KmTmLPHsfvJRw "Controlling Program Flow")
-   [Functions](https://alx-intranet.hbtn.io/rltoken/e3EfHIxICdIncGBwwIDbXQ "Functions")
-   [Objects and Arrays](https://alx-intranet.hbtn.io/rltoken/jg7IbvJpV2oLIKgqOAQH1g "Objects and Arrays")
-   [Intrinsic Objects](https://alx-intranet.hbtn.io/rltoken/jg7IbvJpV2oLIKgqOAQH1g "Intrinsic Objects")
-   [Module patterns](https://alx-intranet.hbtn.io/rltoken/g-MgvO09Ur02RhM63gVyXw "Module patterns")
-   [var, let and const](https://alx-intranet.hbtn.io/rltoken/gJi61GeJTRX0g-M0Rx-0Iw "var, let and const")
-   [JavaScript Tutorial](https://alx-intranet.hbtn.io/rltoken/Y8hkOcy5jO22lQGyF6_NiA "JavaScript Tutorial")
-   [Modern JS](https://alx-intranet.hbtn.io/rltoken/NZawtiBjWUpiojnrtVywNw "Modern JS")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/UFSXQvb7c_45LRd6SdzFTg "explain to anyone"), **without the help of Google**:

### General

-   Why JavaScript programming is amazing
-   How to run a JavaScript script
-   How to create variables and constants
-   What are differences between `var`, `const` and `let`
-   What are all the data types available in JavaScript
-   How to use the `if`, `if ... else` statements
-   How to use comments
-   How to affect values to variables
-   How to use `while` and `for` loops
-   How to use `break` and `continue` statements
-   What is a function and how do you use functions
-   What does a function that does not use any `return` statement return
-   Scope of variables
-   What are the arithmetic operators and how to use them
-   How to manipulate dictionary
-   How to import a file

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/node`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://alx-intranet.hbtn.io/rltoken/1T1yg1vOAChRN20Yyz8crw "Rules of Standard") + [semicolons on top](https://alx-intranet.hbtn.io/rltoken/35q5Pc6A6KWPyd3kGeRQFg "semicolons on top"). Also as reference: [AirBnB style](https://alx-intranet.hbtn.io/rltoken/ilo9MmB3u0utJZjZat-W3Q "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested using `wc`

More Info
---------

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://alx-intranet.hbtn.io/rltoken/35q5Pc6A6KWPyd3kGeRQFg "Documentation")

```
$ sudo npm install semistandard --global

```

## Table of contents
Files | Description
----- | -----------
[0-javascript_is_amazing.js](./0-javascript_is_amazing.js) | JS script that prints “Javascript is amazing”
[1-multi_languages.js](./1-multi_languages.js) | JS script that prints 3 lines
[2-arguments.js](./2-arguments.js) | JS script that prints a message depending of the number of arguments passed
[3-value_argument.js](./3-value_argument.js) | JS script that prints the first argument passed to it
[4-concat.js](./4-concat.js) | JS script that prints two arguments passed to it, in the following format: “ is ”
[5-to_integer.js](./5-to_integer.js) | JS script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
[6-multi_languages_loop.js](./6-multi_languages_loop.js) | JS script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
[7-multi_c.js](./7-multi_c.js) | JS script that prints x times “C is fun”
[8-square.js](./8-square.js) | JS script that prints a square
[9-add.js](./9-add.js) | JS script that prints the addition of 2 integers
[10-factorial.js](./10-factorial.js) | JS script that computes and prints a factorial
[11-second_biggest.js](./11-second_biggest.js) | JS script that searches the second biggest integer in the list of arguments
[12-object.js](./12-object.js) | JS script to replace the value 12 with 89
[13-add.js](./13-add.js) | JS function that returns the addition of 2 integers
[100-let_me_const.js](./100-let_me_const.js) | JS file that modifies the value of myVar (in another file) to 333
[101-call_me_moby.js](./101-call_me_moby.js) | JS function that executes x times a function
[102-add_me_maybe.js](./102-add_me_maybe.js) | JS function that increments and calls a function
[103-object_fct.js](./103-object_fct.js) | JS script that adds a new function incr that increments the integer value of the object myObject
