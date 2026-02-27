<template>
  <div class="mb-8">
    <div class="flex items-center gap-3 mb-2">
      <NuxtLink v-if="backLink" :to="backLink">
        <UButton icon="i-heroicons-arrow-left" color="neutral" variant="ghost" size="sm" />
      </NuxtLink>
      <h1 class="text-3xl font-bold text-gray-900">{{ title }}</h1>
    </div>
    <p v-if="description" class="text-gray-600" :class="{ 'ml-11': backLink }">
      {{ description }}
    </p>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string
  description?: string
  backLink?: string
}

withDefaults(defineProps<Props>(), {
  description: '',
  backLink: '',
})
</script>
