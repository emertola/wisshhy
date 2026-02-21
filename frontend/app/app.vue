<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
// Global app setup
useHead({
  titleTemplate: (title) => title ? `${title} | WishPool` : 'WishPool - Birthday Greetings',
  meta: [
    { name: 'description', content: 'Create beautiful birthday greeting pages and collect heartfelt wishes from friends and family.' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
  ],
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
  ]
})
</script>
