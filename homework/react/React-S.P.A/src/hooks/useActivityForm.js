import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useActivityStore } from '../store/activityStore';
import { validateActivityForm } from '../utils/validation';
import { parseDurationToSeconds, formatDuration } from '../utils/formatting';

export function useActivityForm() {
    const { id } = useParams();
    const navigate = useNavigate();
    const activities = useActivityStore((state) => state.activities);
    const addActivity = useActivityStore((state) => state.addActivity);
    const updateActivity = useActivityStore((state) => state.updateActivity);
    const [errors, setErrors] = useState({});
    const [formData, setFormData] = useState({
        title: '',
        type: '',
        distance: '',
        duration: '',
        dateTime: '',
        description: ''
    });

    useEffect(() => {
        if (id) {
            const existingActivity = activities.find((item) => item.id === id);
            if (existingActivity) {
                setFormData({
                    ...existingActivity,
                    distance: String(existingActivity.distance),
                    duration: formatDuration(existingActivity.duration)
                });
            }
        }
    }, [id, activities]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        const validationErrors = validateActivityForm(formData);
        
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        }

        const seconds = parseDurationToSeconds(formData.duration);

        if (!seconds || isNaN(seconds)) {
            setErrors({ duration: 'Укажите время строго в формате ЧЧ:ММ:СС (например, 00:30:00)' });
            return;
        }
        
        setErrors({});

        const preparedData = {
            ...formData,
            distance: Number(formData.distance),
            duration: seconds
        };
        
        if (id) {
            updateActivity(id, preparedData);
        } else {
            addActivity(preparedData);
        }
        
        navigate('/');
    };

    return {
        id,
        formData,
        errors,
        handleChange,
        handleSubmit,
        navigate
    };
}
