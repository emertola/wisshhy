<template>
  <div>
    <label v-if="label" class="block text-sm font-medium text-gray-700 mb-2">
      {{ label }}
    </label>
    <p v-if="description" class="text-sm text-gray-500 mb-3">
      {{ description }} ({{ images.length }}/{{ maxImages }})
    </p>

    <!-- Upload Area -->
    <div
      v-if="images.length < maxImages"
      @click="triggerUpload"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      :class="[
        'border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-all mb-4',
        isDragging
          ? 'border-purple-500 bg-purple-50'
          : 'border-gray-300 hover:border-purple-400 hover:bg-gray-50',
      ]"
    >
      <UIcon name="i-heroicons-photo" class="w-10 h-10 mx-auto text-gray-400 mb-2" />
      <p class="text-sm text-gray-600 mb-1">
        <span class="text-purple-600 font-medium">Click to upload</span> or drag and drop
      </p>
      <p class="text-xs text-gray-500">You can select multiple images at once</p>
    </div>

    <!-- Images Grid -->
    <div v-if="images.length > 0" class="grid grid-cols-2 sm:grid-cols-3 gap-4">
      <div v-for="(image, index) in images" :key="index" class="relative group">
        <img
          :src="image.preview"
          :alt="`${index + 1}`"
          class="w-full h-32 object-cover rounded-lg"
        />
        <UButton
          icon="i-heroicons-x-mark"
          color="error"
          variant="solid"
          size="xs"
          class="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity"
          @click="removeImage(index)"
          :disabled="disabled"
        />
      </div>
    </div>

    <!-- Hidden file input -->
    <input
      ref="fileInput"
      type="file"
      :accept="accept"
      multiple
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
interface ImageFile {
  file: File
  preview: string
}

interface Props {
  modelValue: ImageFile[]
  label?: string
  description?: string
  accept?: string
  maxSize?: number
  maxImages?: number
  disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  accept: 'image/jpeg,image/png,image/webp',
  maxSize: 5 * 1024 * 1024, // 5MB
  maxImages: 10,
  disabled: false,
})

const emit = defineEmits<{
  'update:modelValue': [images: ImageFile[]]
  error: [message: string]
}>()

const fileInput = ref<HTMLInputElement>()
const isDragging = ref(false)
const error = ref('')

const images = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const triggerUpload = () => {
  fileInput.value?.click()
}

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const files = Array.from(target.files || [])
  validateAndAddImages(files)
}

const handleDrop = (event: DragEvent) => {
  isDragging.value = false
  const files = Array.from(event.dataTransfer?.files || [])
  validateAndAddImages(files)
}

const validateAndAddImages = (files: File[]) => {
  error.value = ''
  const validTypes = new Set(props.accept.split(',').map((t) => t.trim()))

  // Filter valid files
  const validFiles = files.filter((file) => {
    if (!validTypes.has(file.type)) return false
    if (file.size > props.maxSize) return false
    return true
  })

  // Check remaining slots
  const remainingSlots = props.maxImages - images.value.length
  const filesToAdd = validFiles.slice(0, remainingSlots)

  // Add new images
  const newImages = filesToAdd.map((file) => ({
    file,
    preview: URL.createObjectURL(file),
  }))

  images.value = [...images.value, ...newImages]

  // Show warning if some files were skipped
  if (validFiles.length > remainingSlots) {
    error.value = `Only ${remainingSlots} more photos can be added (limit: ${props.maxImages} total)`
    emit('error', error.value)
  }

  // Reset input
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const removeImage = (index: number) => {
  const image = images.value[index]
  if (image?.preview) {
    URL.revokeObjectURL(image.preview)
  }

  const newImages = [...images.value]
  newImages.splice(index, 1)
  images.value = newImages

  error.value = ''
}

// Cleanup on unmount
onUnmounted(() => {
  images.value.forEach((image) => {
    if (image.preview) {
      URL.revokeObjectURL(image.preview)
    }
  })
})
</script>
