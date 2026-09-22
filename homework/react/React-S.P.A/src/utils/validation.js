


export function validateActivityForm(formData) {
    const errors = {}
    if(formData.type ===  "") errors.type = "Вы не выбрали тип спорта!" 
    if(formData.distance <= 0 || !formData.distance) errors.distance = "Дистанция должна быть больше 0!"
    if(!formData.dateTime) errors.dateTime = "Вы не указали дату трениовки!"
    if(!formData.duration) errors.duration = "Вы не указали продолжительность тренировки!" 
    return errors
}