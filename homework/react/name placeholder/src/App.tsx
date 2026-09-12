import React, { useState } from 'react';
import { UserCard } from './components/UserCard';


const App: React.FC = () => {
  const [currentUser] = useState<User>({
    name: 'Алиса',
    age: 28,
    isAdmin: true,
  });

  return (
    <div>
      <h2>Практика: TypeScript в React</h2>
      <UserCard   user={currentUser} />
    </div>
  );
};

export default App;
