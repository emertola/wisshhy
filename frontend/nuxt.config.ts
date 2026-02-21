// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: false },

  modules: [
    '@nuxt/ui',
    // '@pinia/nuxt'
  ],

  // Import Tailwind CSS
  css: ['~/assets/css/main.css'],

  // SSR configuration
  ssr: true,

  // Route rules for SSR/CSR hybrid rendering
  routeRules: {
    // ===== SSR Pages (Public, SEO matters) =====
    '/': { ssr: true }, // Homepage - SEO critical
    // '/view/**': { ssr: true }, // Public birthday reveal - SSR for social sharing
    // '/greetings/**': { ssr: true }, // Contribute page - shareable link

    // // ===== CSR Pages (Behind auth, no SEO) =====
    // '/dashboard': { ssr: false }, // User dashboard
    // '/dashboard/**': { ssr: false }, // Dashboard sub-pages
    // '/login': { ssr: false }, // Login page
    // '/signup': { ssr: false }, // Signup page
    // '/edit/**': { ssr: false }, // Edit greeting page
  },

  // Runtime config for environment variables
  runtimeConfig: {
    public: {
      apiUrl: process.env.NUXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
      googleClientId: process.env.NUXT_PUBLIC_GOOGLE_CLIENT_ID || '',
      appUrl: process.env.NUXT_PUBLIC_APP_URL || 'http://localhost:3000',
    },
  },

  // App configuration
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      title: 'WishPool - Birthday Greetings',
      htmlAttrs: {
        lang: 'en',
      },
    },
  },

  // Color mode configuration for Nuxt UI
  colorMode: {
    preference: 'light',
    fallback: 'light',
    classSuffix: '',
  },
})
