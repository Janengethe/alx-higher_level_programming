## 0x13. JavaScript - Objects, Scopes and Closures

### Resources
* [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
* [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
* [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

### Files Descriptions
* `0-rectangle.js` - creates an empty class `Rectangle` that defines a rectangle
* `1-rectangle.js` - Initializes the instance attribute `width` with the value of `w` and `height` with the value of `h`
* `2-rectangle.js` - If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* `3-rectangle.js` - Creates an instance method called `print()` that prints the rectangle using the character `X`
* `4-rectangle.js` - Creates an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle, and `double()` that multiples the `width` and the `height` of the rectangle by 2
* `5-square.js` - creates a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`
* `6-square.js` - creates a class `Square` that defines a square and inherits from `Square` of `5-square.js`
* `7-occurrences.js` - a function that returns the number of occurrences in a list
* `8-esrever.js` - a function that returns the reversed version of a list. help [source](https://www.codegrepper.com/code-examples/javascript/nodejs+reverse+array)
* `9-logme.js` - a function that prints the number of arguments already printed and the new argument value.
* `10-converter.js` - a function that converts a number from base 10 to another base passed as argument.
* `100-map.js` - a script that imports an array `list` from `100-data.js` and computes a new array. [Tips](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
* `101-sorted.js` - a script that imports a dictionary of occurrences by user id `dict` from `101-data.js` and computes a dictionary of user ids by occurrence.
* `102-concat.js` - a script that concats 2 files, `fileA` and `fileB` and saves the result in `fileC`. [Tips](https://www.programmersought.com/article/54605077814/)
