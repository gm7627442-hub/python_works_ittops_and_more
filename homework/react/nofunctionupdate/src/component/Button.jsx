import { memo } from "react";

export const Button = memo(function ({ onClick, text }) {
  console.log("Render Button");

  return <button onClick={onClick}>{text}</button>;
});

