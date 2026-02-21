<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-50 via-pink-50 to-sky-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-md">
      <!-- Logo/Brand -->
      <div class="text-center mb-8">
        <NuxtLink to="/" class="inline-flex items-center gap-2">
          <span class="text-5xl">🎂</span>
          <span class="text-3xl font-bold text-purple-700">WishPool</span>
        </NuxtLink>
      </div>
      
      <!-- Auth Content -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <slot />
      </div>
      
      <!-- Back to home -->
      <div class="text-center mt-6">
        <NuxtLink 
          to="/" 
          class="text-sm text-gray-600 hover:text-purple-600 transition-colors inline-flex items-center gap-1"
        >
          <UIcon name="i-heroicons-arrow-left" class="w-4 h-4" />
          Back to home
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Layout for authentication pages (login, signup)
// Centered card design with no navbar/footer
</script>
