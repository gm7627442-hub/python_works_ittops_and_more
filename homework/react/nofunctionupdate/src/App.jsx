import { useState, useCallback } from "react";
import { Button } from "./component/Button";


function App() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");

  const handleIncrement = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <h1>useCallback: оптимизация колбэков</h1>

      <p>Счётчик: {count}</p>

      <Button onClick={handleIncrement} text="Увеличить" />

      <p>
        <input
          type="text"
          value={text}
          onChange={(event) => setText(event.target.value)}
        />
      </p>
    </div>
  );
}

export default App;