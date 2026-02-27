<template>
  <div>
    <!-- Hero Section -->
    <section
      class="relative overflow-hidden bg-gradient-to-br from-purple-50 via-pink-50 to-sky-50 py-20 sm:py-32"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <!-- Badge -->
          <div
            class="inline-flex items-center gap-2 bg-purple-100 text-purple-700 px-4 py-2 rounded-full text-sm font-medium mb-8"
          >
            <span class="text-lg">🎉</span>
            <span>Make birthdays unforgettable</span>
          </div>

          <!-- Heading -->
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 mb-6">
            Create Beautiful Birthday
            <span class="text-purple-600 block mt-2">Greeting Pages</span>
          </h1>

          <!-- Subheading -->
          <p class="text-xl text-gray-600 max-w-2xl mx-auto mb-10">
            Collect heartfelt wishes from friends and family in one beautiful place. Share the joy
            with a personalized birthday page.
          </p>

          <!-- CTA Buttons -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <NuxtLink>
              <UButton size="xl" color="primary" class="px-8">
                Get Started Free
                <UIcon name="i-heroicons-arrow-right" class="w-5 h-5 ml-2" />
              </UButton>
            </NuxtLink>
            <UButton size="xl" color="secondary" variant="outline" @click="scrollToHowItWorks">
              See How It Works
            </UButton>
          </div>

          <!-- Social Proof -->
          <div class="mt-12 flex items-center justify-center gap-8 text-sm text-gray-600">
            <div class="flex items-center gap-2">
              <span class="text-2xl">🎂</span>
              <span class="font-medium">500+ pages created</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-2xl">💝</span>
              <span class="font-medium">10,000+ wishes shared</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Decorative Elements -->
      <div
        class="absolute top-20 left-10 text-6xl opacity-20 animate-bounce"
        style="animation-delay: 0s"
      >
        🎈
      </div>
      <div
        class="absolute top-40 right-20 text-5xl opacity-20 animate-bounce"
        style="animation-delay: 1s"
      >
        🎁
      </div>
      <div
        class="absolute bottom-20 left-1/4 text-4xl opacity-20 animate-bounce"
        style="animation-delay: 2s"
      >
        ✨
      </div>
    </section>

    <!-- How It Works Section -->
    <section id="how-it-works" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Section Header -->
        <div class="text-center mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">How It Works</h2>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            Create a memorable birthday surprise in three simple steps
          </p>
        </div>

        <!-- Steps -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
          <!-- Step 1 -->
          <div class="text-center">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-purple-100 text-purple-600 rounded-full text-2xl font-bold mb-6"
            >
              1
            </div>
            <div class="mb-4 text-5xl">📝</div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3">Create a Page</h3>
            <p class="text-gray-600">
              Set up a personalized birthday page with the celebrant's name, photos, and birth date.
            </p>
          </div>

          <!-- Step 2 -->
          <div class="text-center">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-pink-100 text-pink-600 rounded-full text-2xl font-bold mb-6"
            >
              2
            </div>
            <div class="mb-4 text-5xl">🔗</div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3">Share with Friends</h3>
            <p class="text-gray-600">
              Send the contributor link to friends and family so they can write their birthday
              wishes.
            </p>
          </div>

          <!-- Step 3 -->
          <div class="text-center">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-sky-100 text-sky-600 rounded-full text-2xl font-bold mb-6"
            >
              3
            </div>
            <div class="mb-4 text-5xl">🎉</div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3">Surprise the Celebrant</h3>
            <p class="text-gray-600">
              Share the public reveal link with the birthday person to see all the heartfelt
              messages.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Section Header -->
        <div class="text-center mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">Everything You Need</h2>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            Powerful features to make birthday celebrations special
          </p>
        </div>

        <!-- Feature Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <UCard>
            <div class="text-4xl mb-4">🖼️</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Photo Galleries</h3>
            <p class="text-gray-600 text-sm">
              Upload up to 10 beautiful photos of the celebrant to personalize their page.
            </p>
          </UCard>

          <!-- Feature 2 -->
          <UCard>
            <div class="text-4xl mb-4">✉️</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Heartfelt Messages</h3>
            <p class="text-gray-600 text-sm">
              Collect unlimited birthday wishes from friends and family in one place.
            </p>
          </UCard>

          <!-- Feature 3 -->
          <UCard>
            <div class="text-4xl mb-4">🔒</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Private & Secure</h3>
            <p class="text-gray-600 text-sm">
              Your data is safe with secure authentication and private page access.
            </p>
          </UCard>

          <!-- Feature 4 -->
          <UCard>
            <div class="text-4xl mb-4">📱</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Mobile Friendly</h3>
            <p class="text-gray-600 text-sm">
              Perfect experience on any device - desktop, tablet, or phone.
            </p>
          </UCard>

          <!-- Feature 5 -->
          <UCard>
            <div class="text-4xl mb-4">⚡</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Lightning Fast</h3>
            <p class="text-gray-600 text-sm">
              Instant page loads with server-side rendering for the best experience.
            </p>
          </UCard>

          <!-- Feature 6 -->
          <UCard>
            <div class="text-4xl mb-4">🎊</div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Celebration Theme</h3>
            <p class="text-gray-600 text-sm">
              Beautiful, festive design that captures the joy of birthdays.
            </p>
          </UCard>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-br from-purple-600 to-pink-600">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-6">
          Ready to Create Your First Birthday Page?
        </h2>
        <p class="text-xl text-purple-100 mb-10">
          Join hundreds of people making birthdays special with WishPool
        </p>
        <NuxtLink>
          <UButton size="xl" color="neutral" class="px-8">
            Get Started Free
            <UIcon name="i-heroicons-arrow-right" class="w-5 h-5 ml-2" />
          </UButton>
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
// SEO
useHead({
  title: 'Birthday Greetings - Create Beautiful Birthday Wish Pages',
  meta: [
    {
      name: 'description',
      content:
        'Create a personalized birthday page and collect heartfelt wishes from friends and family. Share beautiful memories with your loved ones.',
    },
    // Open Graph
    { property: 'og:title', content: 'WishPool - Birthday Greetings' },
    {
      property: 'og:description',
      content: 'Collect birthday wishes from friends and family in one beautiful page',
    },
    { property: 'og:type', content: 'website' },
    // Twitter
    { name: 'twitter:card', content: 'summary_large_image' },
  ],
})

// Smooth scroll to How It Works
const scrollToHowItWorks = () => {
  const element = document.getElementById('how-it-works')
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<style scoped>
@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

.animate-bounce {
  animation: bounce 3s ease-in-out infinite;
}
</style>
