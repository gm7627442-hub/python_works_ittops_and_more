import { useActivityForm } from '../../hooks/useActivityForm';
import styles from './ActivityForm.module.css';

export function ActivityForm() {
    const { id, formData, errors, handleChange, handleSubmit, navigate } = useActivityForm();

    return (
        <div className={styles.formContainer}>
            <div className={styles.formHeader}>
                <h2 className={styles.formTitle}>
                    {id ? 'Редактировать тренировку' : 'Добавить новую тренировку'}
                </h2>
                <button 
                    type="button" 
                    className={styles.closeButton} 
                    onClick={() => navigate('/')}
                >
                    &times;
                </button>
            </div>
            
            <form onSubmit={handleSubmit}>
                <div className={styles.fieldGroup}>
                    <label>Название:</label>
                    <input 
                        type="text" 
                        name="title" 
                        value={formData.title} 
                        onChange={handleChange} 
                    />
                </div>

                <div className={styles.fieldGroup}>
                    <label>Тип спорта *:</label>
                    <select 
                        name="type" 
                        value={formData.type} 
                        onChange={handleChange}
                    >
                        <option value="">-- Выберите спорт --</option>
                        <option value="run">Бег</option>
                        <option value="walk">Ходьба</option>
                        <option value="cycle">Велосипед</option>
                        <option value="swim">Плавание</option>
                    </select>
                    {errors.type && <span className={styles.error}>{errors.type}</span>}
                </div>

                <div className={styles.fieldGroup}>
                    <label>Дистанция (км) *:</label>
                    <input 
                        type="number" 
                        name="distance" 
                        step="0.01"
                        value={formData.distance} 
                        onChange={handleChange} 
                    />
                    {errors.distance && <span className={styles.error}>{errors.distance}</span>}
                </div>

                <div className={styles.fieldGroup}>
                    <label>Продолжительность (ЧЧ:ММ:СС) *:</label>
                    <input 
                        type="text" 
                        name="duration" 
                        placeholder="00:00:00"
                        value={formData.duration} 
                        onChange={handleChange} 
                    />
                    {errors.duration && <span className={styles.error}>{errors.duration}</span>}
                </div>

                <div className={styles.fieldGroup}>
                    <label>Дата и время *:</label>
                    <input 
                        type="datetime-local" 
                        name="dateTime" 
                        value={formData.dateTime} 
                        onChange={handleChange} 
                    />
                    {errors.dateTime && <span className={styles.error}>{errors.dateTime}</span>}
                </div>

                <div className={styles.fieldGroup}>
                    <label>Заметки:</label>
                    <textarea 
                        name="description" 
                        value={formData.description} 
                        onChange={handleChange} 
                    />
                </div>

                <button type="submit" className={styles.submitButton}>
                    {id ? 'Сохранить изменения' : 'Добавить тренировку'}
                </button>
            </form>
        </div>
    );
}
