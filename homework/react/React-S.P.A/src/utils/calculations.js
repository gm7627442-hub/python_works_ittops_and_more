

export function calculateSpeed(distance, durationInSeconds) {
    const hours = durationInSeconds / 3600;
    const speed = distance / hours;
    
    return Number(speed.toFixed(2));
}

export function calculatePace(distance, durationInSeconds) {
    const secondsPerKm = durationInSeconds / distance;
    const minutes = Math.floor(secondsPerKm / 60);
    const seconds = Math.floor(secondsPerKm % 60)
    const formatredSeconds = String(seconds).padStart(2, '0')
    const finalTime = `${minutes}.${formatredSeconds}`
    
    return finalTime
}