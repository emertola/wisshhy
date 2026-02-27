<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Page Header -->
      <PageHeader
        title="Create Birthday Page"
        description="Create a special page to collect birthday wishes for your loved one"
        back-link="/dashboard"
      />

      <!-- Main Form Card -->
      <UCard>
        <form class="space-y-8" @submit.prevent="handleSubmit">
          <!-- Celebrant Information Section -->
          <FormSection icon="🎂" title="Celebrant Information">
            <!-- Full Name -->
            <div>
              <label for="celebrant-name" class="block text-sm font-medium text-gray-700 mb-1">
                Full Name <span class="text-red-500">*</span>
              </label>
              <UInput
                id="celebrant-name"
                v-model="form.celebrantName"
                placeholder="e.g. John Doe"
                size="lg"
                :disabled="submitting"
                @blur="validateCelebrantName(form.celebrantName)"
              />
              <p v-if="errors.celebrantName" class="mt-1 text-sm text-red-600">
                {{ errors.celebrantName }}
              </p>
            </div>

            <!-- Birth Date -->
            <div>
              <label for="birth-date" class="block text-sm font-medium text-gray-700 mb-1">
                Birth Date <span class="text-red-500">*</span>
              </label>
              <UPopover>
                <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
                  {{
                    form.birthDate
                      ? df.format(form.birthDate.toDate(getLocalTimeZone()))
                      : 'Select a date'
                  }}
                </UButton>
                <template #content>
                  <UCalendar v-model="form.birthDate as CalendarDate" class="p-2" />
                </template>
              </UPopover>

              <p v-if="errors.birthDate" class="mt-1 text-sm text-red-600">
                {{ errors.birthDate }}
              </p>
              <p class="mt-1 text-sm text-gray-500">This will be displayed on the birthday page</p>
            </div>
          </FormSection>

          <!-- Divider -->
          <div class="border-t border-gray-200" />

          <!-- Photos Section -->
          <FormSection icon="📸" title="Photos (Optional)">
            <!-- Cover Photo -->
            <ImageUploader
              v-model="coverPhoto"
              v-model:preview="coverPhotoPreview"
              label="Cover Photo"
              description="This will be the main photo displayed on the birthday page"
              :disabled="submitting"
            />

            <!-- Gallery Photos -->
            <MultiImageUploader
              v-model="galleryPhotos"
              label="Additional Photos"
              description="Add up to 10 photos to create a beautiful gallery"
              :max-images="10"
              :disabled="submitting"
            />
          </FormSection>

          <!-- Form Actions -->
          <FormActions
            :submitting="submitting"
            :is-valid="isFormValid"
            cancel-link="/"
            submit-text="Create Birthday Page"
          />
        </form>
      </UCard>

      <!-- Info Card -->
      <InfoCard />
    </div>
  </div>
</template>

<script setup lang="ts">
import type { CalendarDate } from '@internationalized/date'
import { DateFormatter, getLocalTimeZone } from '@internationalized/date'
import FormActions from '~/components/greeting/FormActions.vue'
import FormSection from '~/components/greeting/FormSection.vue'
import ImageUploader from '~/components/greeting/ImageUploader.vue'
import InfoCard from '~/components/greeting/InfoCard.vue'
import MultiImageUploader from '~/components/greeting/MultiImageUploader.vue'
import PageHeader from '~/components/greeting/PageHeader.vue'
import { useDateUtils } from '~/composables/useDateUtils'
import { useFormValidation } from '~/composables/useFormValidation'

// Page configuration
definePageMeta({
  layout: 'default',
  // middleware: ['auth'] // TODO: Add when ready
})

useHead({
  title: 'Create Birthday Page',
})

// Composables
const { formatDateForAPI } = useDateUtils()
const { errors, validateCelebrantName, validateBirthDate, clearErrors } = useFormValidation()

const df = new DateFormatter('en-US', {
  dateStyle: 'medium',
})

// Form state
const form = reactive({
  celebrantName: '',
  birthDate: undefined as CalendarDate | undefined,
})

// Photo state
const coverPhoto = ref<File | null>(null)
const coverPhotoPreview = ref('')
const galleryPhotos = ref<Array<{ file: File; preview: string }>>([])

// UI state
const submitting = ref(false)
// const maxDate = new Date()

// Computed
const isFormValid = computed(() => {
  return form.celebrantName.trim().length >= 2 && form.birthDate !== undefined
})

// Form submission
const handleSubmit = async () => {
  // Validate all fields
  clearErrors()
  const nameValid = validateCelebrantName(form.celebrantName)
  const dateValid = validateBirthDate(form.birthDate as CalendarDate)

  if (!nameValid || !dateValid) {
    return
  }

  submitting.value = true

  try {
    // Prepare form data
    const formData = new FormData()
    formData.append('celebrant_name', form.celebrantName)
    formData.append('celebrant_birthdate', formatDateForAPI(form.birthDate as CalendarDate) || '')

    if (coverPhoto.value) {
      formData.append('cover_image', coverPhoto.value)
    }

    galleryPhotos.value.forEach((photo) => {
      formData.append('gallery_images', photo.file)
    })

    // TODO: Replace with actual API call
    // const response = await $fetch('/api/v1/greeting-pages', {
    //   method: 'POST',
    //   body: formData
    // })

    // Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 1500))

    console.log('Form submitted:', {
      celebrantName: form.celebrantName,
      birthDate: formatDateForAPI(form.birthDate as CalendarDate),
      coverPhoto: coverPhoto.value?.name,
      galleryPhotos: galleryPhotos.value.length,
    })

    // TODO: Show success toast when ready
    // useToast().add({
    //   title: 'Success!',
    //   description: 'Birthday page created successfully',
    //   color: 'success'
    // })

    // Redirect to dashboard
    await navigateTo('/dashboard')
  } catch (error) {
    console.error('Failed to create greeting page:', error)

    // TODO: Show error toast when ready
    // useToast().add({
    //   title: 'Error',
    //   description: 'Failed to create birthday page. Please try again.',
    //   color: 'error'
    // })
  } finally {
    submitting.value = false
  }
}
</script>
