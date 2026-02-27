<template>
  <footer class="bg-white border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Brand Column -->
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center gap-2 mb-4">
            <span class="text-3xl">🎂</span>
            <span class="text-2xl font-bold text-purple-700">WishPool</span>
          </div>
          <p class="text-gray-600 text-sm max-w-md">
            Create beautiful birthday greeting pages and collect heartfelt wishes from friends and
            family. Make every birthday special with WishPool.
          </p>
        </div>

        <!-- Product Links -->
        <div>
          <h3 class="font-semibold text-gray-900 mb-4">Product</h3>
          <ul class="space-y-2">
            <li>
              <NuxtLink
                to="/#how-it-works"
                class="text-gray-600 hover:text-purple-600 text-sm transition-colors"
              >
                How It Works
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                to="/#features"
                class="text-gray-600 hover:text-purple-600 text-sm transition-colors"
              >
                Features
              </NuxtLink>
            </li>
            <li>
              <NuxtLink class="text-gray-600 hover:text-purple-600 text-sm transition-colors">
                Dashboard
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Company Links -->
        <div>
          <h3 class="font-semibold text-gray-900 mb-4">Company</h3>
          <ul class="space-y-2">
            <li>
              <NuxtLink class="text-gray-600 hover:text-purple-600 text-sm transition-colors">
                About
              </NuxtLink>
            </li>
            <li>
              <NuxtLink class="text-gray-600 hover:text-purple-600 text-sm transition-colors">
                Privacy
              </NuxtLink>
            </li>
            <li>
              <NuxtLink class="text-gray-600 hover:text-purple-600 text-sm transition-colors">
                Terms
              </NuxtLink>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div
        class="mt-8 pt-8 border-t border-gray-200 flex flex-col sm:flex-row justify-between items-center gap-4"
      >
        <p class="text-sm text-gray-600">© {{ currentYear }} WishPool. All rights reserved.</p>
        <div class="flex items-center gap-6">
          <a href="#" class="text-gray-400 hover:text-purple-600 transition-colors">
            <span class="sr-only">Twitter</span>
            <UIcon name="i-heroicons-x-mark" class="w-5 h-5" />
          </a>
          <a href="#" class="text-gray-400 hover:text-purple-600 transition-colors">
            <span class="sr-only">Instagram</span>
            <UIcon name="i-heroicons-camera" class="w-5 h-5" />
          </a>
          <a href="#" class="text-gray-400 hover:text-purple-600 transition-colors">
            <span class="sr-only">GitHub</span>
            <UIcon name="i-heroicons-code-bracket" class="w-5 h-5" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const currentYear = new Date().getFullYear()
</script>
