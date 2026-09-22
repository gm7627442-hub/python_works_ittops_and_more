import { create } from 'zustand'

export const useActivityStore = create((set) => ({

    activities: [],

    addActivity: (newActivity) => set((state) => {
        const activityWithId = { ...newActivity, id: crypto.randomUUID() };
        const updatedActivities = [...state.activities, activityWithId];
        updatedActivities.sort((a, b) => new Date(b.dateTime) - new Date(a.dateTime));

        return { activities: updatedActivities };

    }),

    updateActivity: (id, updatedData) => set((state) => {

        const updatedActivities = state.activities.map((activity) => {
            if (activity.id === id) {
                return { ...activity, ...updatedData };
            }
            return activity;
        });

        updatedActivities.sort((a, b) => new Date(b.dateTime) - new Date(a.dateTime));

        return { activities: updatedActivities };
    })
}));