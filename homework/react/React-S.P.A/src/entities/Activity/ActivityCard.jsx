import { memo } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './ActivityCard.module.css';
import { calculateSpeed, calculatePace } from '../../utils/calculations';
import { generateActivityName } from '../../utils/activity';

import iconRun from '../../assets/run.png';
import iconWalk from '../../assets/walk.png';
import iconSwim from '../../assets/swim.png';
import iconCycle from '../../assets/cycle.png';



const badgeConfig = {
    run: { label: 'Бег', img: iconRun, className: styles.badgeRun },
    walk: { label: 'Ходьба', img: iconWalk, className: styles.badgeWalk },
    cycle: { label: 'Велосипед', img: iconCycle, className: styles.badgeCycle },
    swim: { label: 'Плавание', img: iconSwim, className: styles.badgeSwim }
};

function ActivityCard({ activity }) {
    const speed = calculateSpeed(activity.distance, activity.duration);
    const pace = calculatePace(activity.distance, activity.duration);
    const navigate = useNavigate();
    const activityName = generateActivityName(activity.type, activity.dateTime);
    
    const badge = badgeConfig[activity.type] || { label: 'Спорт', img: null, className: styles.badgeDefault };

    return (
        <div className={styles.card}>
            <div className={styles.cardHeader}>
                <h3>{activity.title || activityName}</h3>
                <span className={`${styles.badge} ${badge.className}`}>
                    {badge.img && (
                        <img 
                            src={badge.img} 
                            alt={badge.label} 
                            className={styles.badgeIcon} 
                        />
                    )}
                    {badge.label}
                </span>
            </div>
            
            <p>{activity.description}</p>
            <p className={styles.distance}>Дистанция: {activity.distance} км</p>
            <p className={styles.speed}>Скорость: {speed} км/ч</p>
            <p className={styles.pace}>Темп: {pace} на км</p>
            <p className={styles.date}>Дата: {new Date(activity.dateTime).toLocaleString()}</p>
            
            <button 
                className={styles.editButton} 
                onClick={() => navigate(`/activities/edit/${activity.id}`)}
            >
                Редактировать
            </button>
        </div>
    );
}

export default memo(ActivityCard);
