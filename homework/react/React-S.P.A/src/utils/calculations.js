

export function calculateSpeed(distance, durationInSeconds) {
    const hours = durationInSeconds / 3600;
    const speed = distance / hours;
    
    return Number(speed.toFixed(2));
}

export function calculatePace(distanceKm, durationSeconds) {
    if (!distanceKm || !durationSeconds || distanceKm <= 0) {
        return '0 мин 00 сек';
    }

    const totalSecondsPerKm = durationSeconds / distanceKm;
    const minutes = Math.floor(totalSecondsPerKm / 60);
    const seconds = Math.round(totalSecondsPerKm % 60);

    const formattedSeconds = String(seconds).padStart(2, '0');

    return `${minutes} мин ${formattedSeconds} сек`;
}
