import type { CalendarDate } from '@internationalized/date'

interface ValidationErrors {
  [key: string]: string
}

export const useFormValidation = () => {
  const errors = ref<ValidationErrors>({})

  const validateCelebrantName = (name: string): boolean => {
    if (!name.trim()) {
      errors.value.celebrantName = 'Celebrant name is required'
      return false
    }

    if (name.trim().length < 2) {
      errors.value.celebrantName = 'Name must be at least 2 characters'
      return false
    }

    delete errors.value.celebrantName
    return true
  }

  const validateBirthDate = (birthDate: CalendarDate | undefined): boolean => {
    if (!birthDate) {
      errors.value.birthDate = 'Birth date is required'
      return false
    }

    const today = new Date()
    const selectedDate = new Date(birthDate.year, birthDate.month - 1, birthDate.day)

    if (selectedDate > today) {
      errors.value.birthDate = 'Birth date cannot be in the future'
      return false
    }

    delete errors.value.birthDate
    return true
  }

  const clearErrors = () => {
    errors.value = {}
  }

  const clearError = (field: string) => {
    delete errors.value[field]
  }

  return {
    errors: readonly(errors),
    validateCelebrantName,
    validateBirthDate,
    clearErrors,
    clearError,
  }
}
