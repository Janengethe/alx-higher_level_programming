#!/usr/bin/node
exports.converter = function (base) {
  function conv (args) {
    return args.toString(base);
  }
  return (conv);
};
