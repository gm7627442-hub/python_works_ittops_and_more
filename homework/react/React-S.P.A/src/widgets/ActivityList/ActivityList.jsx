import { useActivityStore } from '../../store/activityStore';
import ActivityCard from '../../entities/Activity/ActivityCard';
import styles from './ActivityList.module.css';

export function ActivityList() {
    const activities = useActivityStore((state) => state.activities);
    if(activities.length === 0 ) 
        return <p>Тренировок пока нет!</p>

return <div className={styles.list}>
            {activities.map((activity) => (
                <ActivityCard activity={activity} key={activity.id}/>
            ))}
        </div>
}