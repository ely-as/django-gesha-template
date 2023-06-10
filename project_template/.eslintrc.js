module.exports = {
  extends: ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
  parser: "@typescript-eslint/parser",
  plugins: ["@typescript-eslint"],
  rules: {
    indent: ["error", 2],
    quotes: ["error", "double"]
  },
  root: true
};
