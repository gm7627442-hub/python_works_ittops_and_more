import React, { useState } from 'react';

export interface User {
  name: string;
  age: number;
  isAdmin: boolean;
}

interface UserCardProps {
  user: User;
}

export const UserCard: React.FC<UserCardProps> = ({ user }) => {
  const [showDetails] = useState<boolean>(true);

  return (
    <div>
      <h3>{user.name}</h3>
      {showDetails && (
        <div>
          <div>Возраст: {user.age}</div>
          <div>Роль: {user.isAdmin ? 'Администратор' : 'Пользователь'}</div>
        </div>
      )}
    </div>
  );
};

