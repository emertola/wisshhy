<template>
  <div class="flex items-center justify-between pt-6 border-t border-gray-200">
    <NuxtLink :to="cancelLink">
      <UButton color="neutral" variant="ghost" :disabled="submitting"> Cancel </UButton>
    </NuxtLink>

    <UButton
      type="submit"
      color="primary"
      size="lg"
      :loading="submitting"
      :disabled="!isValid || submitting"
    >
      <UIcon v-if="icon" :name="icon" class="w-5 h-5 mr-2" />
      {{ submitText }}
    </UButton>
  </div>
</template>

<script setup lang="ts">
interface Props {
  submitting: boolean
  isValid: boolean
  cancelLink: string
  submitText: string
  icon?: string
}

withDefaults(defineProps<Props>(), {
  icon: 'i-heroicons-sparkles',
})
</script>
