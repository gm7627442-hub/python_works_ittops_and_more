

export function generateActivityName(type, dateTime){
const activityMap = {
    run: {
        name: 'пробежка',
        morning: 'Утренняя',
        day: 'Дневная',
        evening: 'Вечерняя',
        night: 'Ночная'
    },
    walk: {
        name: 'ходьба',
        morning: 'Утренняя',
        day: 'Дневная',
        evening: 'Вечерняя',
        night: 'Ночная'
    },
    cycle: {
        name: 'велосипед',
        morning: 'Утренний',
        day: 'Дневной',
        evening: 'Вечерний',
        night: 'Ночной'
    },
    swim: {
        name: 'плавание',
        morning: 'Утреннее',
        day: 'Дневное',
        evening: 'Вечернее',
        night: 'Ночное'
    }
};
    const hours = new Date(dateTime).getHours();
    let timeOfDay = "placeholder"
    
    if (hours >= 5 && hours < 12) timeOfDay = "morning";
    else if (hours >= 12 && hours < 17) timeOfDay = "day";
    else if (hours >= 17 && hours < 24) timeOfDay = "evening";
    else timeOfDay = "night";
    
    const sportData = activityMap[type];
    const prefix = sportData[timeOfDay]; 
    const name = sportData.name; 

return `${prefix} ${name}`
}


