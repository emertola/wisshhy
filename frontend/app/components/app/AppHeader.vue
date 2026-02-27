<script setup lang="ts">
import type { close } from 'node:fs'

const mobileMenuOpen = ref(false)
const loggingOut = ref(false)

// TODO: Replace with actual auth state from Pinia store
const isAuthenticated = ref(false)

const handleLogout = async () => {
  loggingOut.value = true
  try {
    // TODO: Implement logout logic
    // await authStore.logout()
    await new Promise((resolve) => setTimeout(resolve, 500)) // Simulate API call
    mobileMenuOpen.value = false
    // navigateTo("/login");
  } catch (error) {
    console.error('Logout failed:', error)
  } finally {
    loggingOut.value = false
  }
}
</script>

<template>
  <header class="bg-white border-b border-gray-200 sticky top-0 z-50 backdrop-blur-sm bg-white/90">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo / Brand -->
        <NuxtLink to="/" class="flex items-center gap-2 hover:opacity-80 transition-opacity">
          <span class="text-3xl">🎂</span>
          <span class="text-2xl font-bold text-purple-700">WishPool</span>
        </NuxtLink>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-6">
          <NuxtLink
            to="/#how-it-works"
            class="text-gray-600 hover:text-purple-600 transition-colors font-medium"
          >
            How It Works
          </NuxtLink>
          <NuxtLink
            to="/#features"
            class="text-gray-600 hover:text-purple-600 transition-colors font-medium"
          >
            Features
          </NuxtLink>

          <!-- Auth State -->
          <template v-if="isAuthenticated">
            <NuxtLink class="text-gray-600 hover:text-purple-600 transition-colors font-medium">
              My Pages
            </NuxtLink>
            <UButton color="primary" variant="soft" @click="handleLogout" :loading="loggingOut">
              Log Out
            </UButton>
          </template>
          <template v-else>
            <NuxtLink>
              <UButton color="secondary" variant="ghost"> Log In </UButton>
            </NuxtLink>
            <NuxtLink>
              <UButton color="primary"> Get Started </UButton>
            </NuxtLink>
          </template>
        </div>

        <!-- Mobile Menu Button -->
        <div class="block md:hidden">
          <UButton
            color="secondary"
            variant="ghost"
            icon="i-heroicons-bars-3"
            @click="mobileMenuOpen = true"
          />
        </div>
      </div>
    </nav>

    <!-- Mobile Menu Slideover -->
    <USlideover v-model:open="mobileMenuOpen" :close="false">
      <template #body>
        <div class="flex flex-col h-full md:hidden">
          <!-- Header -->
          <div class="flex items-center justify-between p-6 border-b border-gray-200">
            <div class="flex items-center gap-2">
              <span class="text-3xl">🎂</span>
              <span class="text-2xl font-bold text-purple-700">WishPool</span>
            </div>
            <UButton
              color="neutral"
              variant="ghost"
              icon="i-heroicons-x-mark"
              @click="mobileMenuOpen = false"
              aria-label="Close menu"
            />
          </div>

          <!-- Navigation Links -->
          <div class="flex flex-col gap-4 p-6 flex-1">
            <NuxtLink
              to="/#how-it-works"
              @click="mobileMenuOpen = false"
              class="text-lg text-gray-700 hover:text-purple-600 transition-colors py-2"
            >
              How It Works
            </NuxtLink>
            <NuxtLink
              to="/#features"
              @click="mobileMenuOpen = false"
              class="text-lg text-gray-700 hover:text-purple-600 transition-colors py-2"
            >
              Features
            </NuxtLink>

            <template v-if="isAuthenticated">
              <NuxtLink
                @click="mobileMenuOpen = false"
                class="text-lg text-gray-700 hover:text-purple-600 transition-colors py-2"
              >
                My Pages
              </NuxtLink>
            </template>

            <!-- Auth Buttons -->
            <div class="border-t border-gray-200 pt-6 mt-auto space-y-3">
              <template v-if="isAuthenticated">
                <UButton color="primary" block @click="handleLogout" :loading="loggingOut">
                  Log Out
                </UButton>
              </template>
              <template v-else>
                <NuxtLink @click="mobileMenuOpen = false">
                  <UButton color="neutral" variant="outline" block> Log In </UButton>
                </NuxtLink>
                <NuxtLink @click="mobileMenuOpen = false">
                  <UButton color="primary" block> Get Started </UButton>
                </NuxtLink>
              </template>
            </div>
          </div>
        </div>
      </template>
    </USlideover>
  </header>
</template>
