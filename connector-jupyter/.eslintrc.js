module.exports = {
  env: {
    browser: true,
    worker: true,
    amd: true,
    webextensions: true,
  },
  extends: [
    'airbnb-base',
  ],
  parserOptions: {
    impliedStrict: true,
  },
  parser: "babel-eslint",
  rules: {
    "import/no-amd": "off",
    "max-len": ["warn", 120],
    "object-curly-newline": ["warn", { ObjectPattern: { multiline: true } }],
    "no-param-reassign": ["error", { props: false }],
    "no-unused-expressions": ["error", { allowShortCircuit: true }],
    "func-names": "off",
    "no-console": "off",
    "no-nested-ternary": "off",
    "lines-between-class-members": ["error", "always", { exceptAfterSingleLine: true }],
    "no-underscore-dangle": ["error", { allowAfterThis: true, allow: ['_id', '_insert_element_at_index'] }],
    "class-methods-use-this": "off",
  },
};
