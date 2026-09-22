import { create } from 'zustand';

export const useCounterStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  multuplay: () => set((state) => ({ count: state.count * 2 })),
  divide: () => set((state) => ({ count: state.count / 2 })),
  reset: () => set({ count: 0 }),
}));

