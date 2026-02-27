import { CalendarDate, type DateValue } from '@internationalized/date'

export const useDateUtils = () => {
  /**
   * Get today's date as CalendarDate
   */
  const getToday = (): CalendarDate => {
    const today = new Date()
    return new CalendarDate(today.getFullYear(), today.getMonth() + 1, today.getDate())
  }

  /**
   * Format DateValue to YYYY-MM-DD string for API
   */
  const formatDateForAPI = (date: DateValue | undefined): string | null => {
    if (!date) return null

    const year = date.year
    const month = String(date.month).padStart(2, '0')
    const day = String(date.day).padStart(2, '0')

    return `${year}-${month}-${day}`
  }

  /**
   * Convert CalendarDate to JavaScript Date
   */
  const calendarDateToDate = (calendarDate: DateValue): Date => {
    return new Date(calendarDate.year, calendarDate.month - 1, calendarDate.day)
  }

  /**
   * Convert JavaScript Date to CalendarDate
   */
  const dateToCalendarDate = (date: Date): CalendarDate => {
    return new CalendarDate(date.getFullYear(), date.getMonth() + 1, date.getDate())
  }

  return {
    getToday,
    formatDateForAPI,
    calendarDateToDate,
    dateToCalendarDate,
  }
}
