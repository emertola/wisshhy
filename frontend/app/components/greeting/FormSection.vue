<template>
  <div>
    <h2 class="text-xl font-semibold text-gray-900 mb-4 flex items-center gap-2">
      <span v-if="icon" class="text-2xl">{{ icon }}</span>
      {{ title }}
    </h2>
    <div class="space-y-4">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string
  icon?: string
}

withDefaults(defineProps<Props>(), {
  icon: '',
})
</script>
