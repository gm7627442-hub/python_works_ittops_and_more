
export function parseDurationToSeconds(timeString) {
    const [hours, minutes, seconds] = timeString.split(':')
    const summary = Number(hours) * 3600 + Number(minutes) * 60 + Number(seconds)

return summary
}

export function formatDuration(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor(seconds % 3600 / 60);
    const remSeconds = Math.floor(seconds % 60);
    const finalTimeString = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(remSeconds).padStart(2, '0')}`;

    return finalTimeString 
}