// @ts-check
import withNuxt from './.nuxt/eslint.config.mjs'
import eslintConfigPrettier from 'eslint-config-prettier'

export default withNuxt(
  {
    rules: {
      // Enforce single quotes
      quotes: ['error', 'single'],

      // Always require parentheses for arrow functions
      'arrow-parens': ['error', 'always'],
    },
  },

  // Disable ESLint formatting rules that conflict with Prettier
  eslintConfigPrettier
)
