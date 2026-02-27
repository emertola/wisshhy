<template>
  <div>
    <label v-if="label" class="block text-sm font-medium text-gray-700 mb-2">
      {{ label }}
    </label>
    <p v-if="description" class="text-sm text-gray-500 mb-3">
      {{ description }}
    </p>

    <!-- Upload Area (when no file) -->
    <div
      v-if="!preview"
      @click="triggerUpload"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      :class="[
        'border-2 border-dashed rounded-lg text-center cursor-pointer transition-all',
        isDragging
          ? 'border-purple-500 bg-purple-50'
          : 'border-gray-300 hover:border-purple-400 hover:bg-gray-50',
        size === 'sm' ? 'p-6' : 'p-8',
      ]"
    >
      <UIcon
        name="i-heroicons-photo"
        :class="['mx-auto text-gray-400 mb-3', size === 'sm' ? 'w-10 h-10' : 'w-12 h-12']"
      />
      <p class="text-sm text-gray-600 mb-1">
        <span class="text-purple-600 font-medium">Click to upload</span> or drag and drop
      </p>
      <p class="text-xs text-gray-500">{{ acceptedFormats }}</p>
    </div>

    <!-- Preview (when file exists) -->
    <div v-else class="relative">
      <img
        :src="preview"
        :alt="alt"
        :class="['w-full object-cover rounded-lg', size === 'sm' ? 'h-32' : 'h-64']"
      />
      <UButton
        icon="i-heroicons-x-mark"
        color="error"
        variant="solid"
        :size="size === 'sm' ? 'xs' : 'sm'"
        :class="[
          'absolute transition-opacity',
          size === 'sm' ? 'top-1 right-1' : 'top-2 right-2',
          removeOnHover ? 'opacity-0 group-hover:opacity-100' : '',
        ]"
        @click="handleRemove"
        :disabled="disabled"
      />
    </div>

    <!-- Hidden file input -->
    <input
      ref="fileInput"
      type="file"
      :accept="accept"
      :multiple="multiple"
      class="hidden"
      @change="handleFileChange"
      :disabled="disabled"
    />

    <!-- Error message -->
    <p v-if="error" class="mt-2 text-sm text-red-600">
      {{ error }}
    </p>
  </div>
</template>

<script setup lang="ts">
interface Props {
  modelValue?: File | null
  preview?: string
  label?: string
  description?: string
  accept?: string
  maxSize?: number // in bytes
  multiple?: boolean
  disabled?: boolean
  size?: 'sm' | 'md'
  alt?: string
  removeOnHover?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: null,
  preview: '',
  accept: 'image/jpeg,image/png,image/webp',
  maxSize: 5 * 1024 * 1024, // 5MB default
  multiple: false,
  disabled: false,
  size: 'md',
  alt: 'Uploaded image',
  removeOnHover: false,
})

const emit = defineEmits<{
  'update:modelValue': [file: File | null]
  'update:preview': [preview: string]
  error: [message: string]
  remove: []
}>()

const fileInput = ref<HTMLInputElement>()
const isDragging = ref(false)
const error = ref('')

const acceptedFormats = computed(() => {
  const formats = props.accept
    .split(',')
    .map((type) => {
      const format = type.split('/')[1]?.toUpperCase()
      return format
    })
    .join(', ')
  return `${formats} up to ${Math.round(props.maxSize / (1024 * 1024))}MB`
})

const triggerUpload = () => {
  fileInput.value?.click()
}

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (file) {
    validateAndSetFile(file)
  }
}

const handleDrop = (event: DragEvent) => {
  isDragging.value = false
  const file = event.dataTransfer?.files[0]
  if (file) {
    validateAndSetFile(file)
  }
}

const validateAndSetFile = (file: File) => {
  error.value = ''

  // Validate file type
  const validTypes = props.accept.split(',').map((t) => t.trim())
  if (!validTypes.includes(file.type)) {
    const formats = validTypes.map((t) => t.split('/')[1]?.toUpperCase()).join(', ')
    error.value = `Please upload a valid image (${formats})`
    emit('error', error.value)
    return
  }

  // Validate file size
  if (file.size > props.maxSize) {
    const sizeMB = Math.round(props.maxSize / (1024 * 1024))
    error.value = `Image must be less than ${sizeMB}MB`
    emit('error', error.value)
    return
  }

  // Emit file and preview
  const previewUrl = URL.createObjectURL(file)
  emit('update:modelValue', file)
  emit('update:preview', previewUrl)
}

const handleRemove = () => {
  if (props.preview) {
    URL.revokeObjectURL(props.preview)
  }

  emit('update:modelValue', null)
  emit('update:preview', '')
  emit('remove')

  if (fileInput.value) {
    fileInput.value.value = ''
  }

  error.value = ''
}

// Cleanup on unmount
onUnmounted(() => {
  if (props.preview) {
    URL.revokeObjectURL(props.preview)
  }
})
</script>
