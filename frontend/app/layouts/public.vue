<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-orange-50">
    <!-- Minimal header with logo only -->
    <header class="bg-white/80 backdrop-blur-sm border-b border-purple-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <NuxtLink to="/" class="inline-flex items-center gap-2 hover:opacity-80 transition-opacity">
          <span class="text-3xl">🎂</span>
          <span class="text-2xl font-bold text-purple-700">WishPool</span>
        </NuxtLink>
      </div>
    </header>
    
    <!-- Main Content (full width, no container) -->
    <main>
      <slot />
    </main>
    
    <!-- Minimal footer -->
    <footer class="bg-white/50 backdrop-blur-sm border-t border-purple-100 mt-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <p class="text-center text-sm text-gray-600">
          Create your own greeting page at 
          <NuxtLink to="/" class="text-purple-600 hover:text-purple-700 font-medium">
            WishPool
          </NuxtLink>
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
// Minimal layout for public reveal pages
// No navigation, just branding and content
</script>
