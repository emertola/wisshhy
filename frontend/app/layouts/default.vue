<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <!-- Header / Navbar -->
    <AppHeader />
    
    <!-- Main Content -->
    <main class="flex-1">
      <slot />
    </main>
    
    <!-- Footer -->
    <AppFooter />
  </div>
</template>

<script setup lang="ts">
// This is the default layout used by most pages
// Pages can override by setting: definePageMeta({ layout: 'other' })
</script>
