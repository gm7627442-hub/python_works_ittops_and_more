import { useNavigate } from "react-router-dom";
import { ActivityList } from '../../widgets/ActivityList/ActivityList';
import { Header } from '../../widgets/Header/Header'; // <-- Добавили импорт шапки
import styles from './ActivitiesPage.module.css';

export function ActivitiesPage() {
    const navigate = useNavigate();

    return (
        <div>
            <Header /> 
            <div> 
                <button 
                    className={styles.editButton} 
                    onClick={() => navigate('/activities/new')}
                >
                    Добавить тренировку
                </button>
                <ActivityList />
            </div>
        </div>
    );
}
