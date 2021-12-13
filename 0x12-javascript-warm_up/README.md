## 0x12. JavaScript - Warm up

### Resources
* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)
* [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

### Requirements
* All files interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* Code is `semistandard` compliant (version 14.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)


### Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard
[Documentation](https://github.com/standard/semistandard)

`$ sudo npm install semistandard --global`

### Files Descriptions
* `0-javascript_is_amazing.js`- a script that prints "JavaScript is` - a script that prints `x` times "C is fun"
* `1-multi_languages.js` - a script that prints 3 lines:The first line: “C is fun”The second line: “Python is cool”The third line: “JavaScript is amazing”
* `2-arguments.js` - a script that prints a message depending of the number of arguments passed
* `3-value_argument.js` - a script that prints the first argument passed to it
* `4-concat.js` - a script that prints two arguments passed to it, in the following format: “ is ”
* `5-to_integer.js` - a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
 * `6-multi_languages_loop.js` - a script that prints 3 lines
* `7-multi_c.js` - a script that prints x times “C is fun”
* `8-square.js` - a script that prints a square
* `9-add.js` - a script that prints the addition of 2 integers
* `10-factorial.js` - a script that computes and prints a factorial
* `11-second_biggest.js` - a script that searches the second biggest integer in the list of arguments.
* `12-object.js` - Updates this script to replace the value 12 with 89:
```
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
```
* `13-add.js` - a function that returns the addition of 2 integers
* `100-let_me_const.js` - a file that modifies the value of `myVar` to `333`
* `101-call_me_moby.js` - a function that executes `x` times a function.
* `102-add_me_maybe.js` - a function that increments and calls a function.
* `103-object_fct.js` - Updates this script by adding a new function `incr` that increments the integer `value`.
```
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```
