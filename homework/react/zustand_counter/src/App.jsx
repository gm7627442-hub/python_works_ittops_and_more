import { useCounterStore } from "./useCounterStore";

function App() {
  const count = useCounterStore((state) => state.count);
  const increment = useCounterStore((state) => state.increment);
  const decrement = useCounterStore((state) => state.decrement);
  const reset = useCounterStore((state) => state.reset);
  const multyplay = useCounterStore((state) => state.multyplay);
  const divide = useCounterStore((state) => state.divide);

  return (
    <div>
      <div>{count}</div>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>0</button>
      <button onClick={increment}>+</button>
      <button onClick={divide}>/</button>
      <button onClick={multyplay}>*</button>
    </div>
  );
}



export default App;

